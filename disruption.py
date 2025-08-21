#!/usr/bin/env python3
"""
Cursor Disruption Module
Simulates malware behavior by randomly moving or hiding the mouse pointer
to mimic attacker distraction tactics during data exfiltration.
"""

import pyautogui
import threading
import time
import random
import sys
import os
from datetime import datetime
import logging

# Platform-specific imports
try:
    if sys.platform == "win32":
        import ctypes
        from ctypes import wintypes
    elif sys.platform == "darwin":  # macOS
        import subprocess
    elif sys.platform.startswith("linux"):
        import subprocess
except ImportError as e:
    print(f"Warning: Platform-specific imports failed: {e}")

class CursorDisruptionModule:
    """
    A module that simulates malware cursor disruption behavior.
    Randomly moves or hides the cursor to mimic attacker distraction tactics.
    """
    
    def __init__(self, log_file="cursor_disruption.log"):
        self.running = False
        self.disruption_thread = None
        self.log_file = log_file
        self.setup_logging()
        
        # Disruption patterns
        self.disruption_patterns = {
            'random_movement': self.random_movement,
            'hide_cursor': self.hide_cursor,
            'show_cursor': self.show_cursor,
            'rapid_movement': self.rapid_movement,
            'corner_hiding': self.corner_hiding
        }
        
        # Configuration
        self.config = {
            'movement_range': (50, 200),  # pixels
            'disruption_interval': (5, 15),  # seconds
            'disruption_duration': (1, 3),  # seconds
            'trigger_probability': 0.3,  # 30% chance per interval
            'keyboard_triggers': ['ctrl', 'alt', 'shift']  # keys that trigger disruption
        }
        
        # Store original cursor position
        self.original_position = None
        
    def setup_logging(self):
        """Setup logging for cursor disruption activities."""
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
    def log_disruption(self, action, details=""):
        """Log cursor disruption activities."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Cursor Disruption: {action}"
        if details:
            log_entry += f" - {details}"
        logging.info(log_entry)
        print(f"🔧 {log_entry}")
        
    def get_screen_size(self):
        """Get current screen dimensions."""
        try:
            return pyautogui.size()
        except Exception as e:
            self.log_disruption("ERROR", f"Failed to get screen size: {e}")
            return (1920, 1080)  # fallback
            
    def random_movement(self):
        """Move cursor to random position within movement range."""
        try:
            current_pos = pyautogui.position()
            screen_width, screen_height = self.get_screen_size()
            
            # Calculate random movement within range
            range_min, range_max = self.config['movement_range']
            movement_x = random.randint(-range_max, range_max)
            movement_y = random.randint(-range_max, range_max)
            
            new_x = max(0, min(screen_width, current_pos[0] + movement_x))
            new_y = max(0, min(screen_height, current_pos[1] + movement_y))
            
            pyautogui.moveTo(new_x, new_y, duration=0.1)
            self.log_disruption("Random Movement", f"({current_pos[0]},{current_pos[1]}) -> ({new_x},{new_y})")
            
        except Exception as e:
            self.log_disruption("ERROR", f"Random movement failed: {e}")
            
    def hide_cursor(self):
        """Hide the cursor using platform-specific methods."""
        try:
            if sys.platform == "win32":
                # Windows: Use ctypes to hide cursor
                ctypes.windll.user32.ShowCursor(False)
                self.log_disruption("Hide Cursor", "Windows API")
                
            elif sys.platform == "darwin":
                # macOS: Use osascript to hide cursor
                subprocess.run(['osascript', '-e', 'tell application "System Events" to set cursor to none'], 
                            capture_output=True)
                self.log_disruption("Hide Cursor", "macOS System Events")
                
            elif sys.platform.startswith("linux"):
                # Linux: Use xdotool to hide cursor (if available)
                try:
                    subprocess.run(['xdotool', 'mousemove', '0', '0'], capture_output=True)
                    subprocess.run(['xdotool', 'mousemove', '--screen', '0', '9999', '9999'], capture_output=True)
                    self.log_disruption("Hide Cursor", "Linux xdotool")
                except FileNotFoundError:
                    self.log_disruption("WARNING", "xdotool not available on Linux")
                    
        except Exception as e:
            self.log_disruption("ERROR", f"Hide cursor failed: {e}")
            
    def show_cursor(self):
        """Show the cursor using platform-specific methods."""
        try:
            if sys.platform == "win32":
                # Windows: Use ctypes to show cursor
                ctypes.windll.user32.ShowCursor(True)
                self.log_disruption("Show Cursor", "Windows API")
                
            elif sys.platform == "darwin":
                # macOS: Use osascript to show cursor
                subprocess.run(['osascript', '-e', 'tell application "System Events" to set cursor to arrow'], 
                            capture_output=True)
                self.log_disruption("Show Cursor", "macOS System Events")
                
            elif sys.platform.startswith("linux"):
                # Linux: Move cursor back to visible area
                try:
                    subprocess.run(['xdotool', 'mousemove', '100', '100'], capture_output=True)
                    self.log_disruption("Show Cursor", "Linux xdotool")
                except FileNotFoundError:
                    self.log_disruption("WARNING", "xdotool not available on Linux")
                    
        except Exception as e:
            self.log_disruption("ERROR", f"Show cursor failed: {e}")
            
    def rapid_movement(self):
        """Perform rapid cursor movements to create distraction."""
        try:
            screen_width, screen_height = self.get_screen_size()
            
            # Perform 3-5 rapid movements
            for i in range(random.randint(3, 5)):
                x = random.randint(0, screen_width)
                y = random.randint(0, screen_height)
                pyautogui.moveTo(x, y, duration=0.05)
                time.sleep(0.1)
                
            self.log_disruption("Rapid Movement", f"{i+1} movements")
            
        except Exception as e:
            self.log_disruption("ERROR", f"Rapid movement failed: {e}")
            
    def corner_hiding(self):
        """Move cursor to screen corners to hide it."""
        try:
            screen_width, screen_height = self.get_screen_size()
            corners = [
                (0, 0),  # top-left
                (screen_width-1, 0),  # top-right
                (0, screen_height-1),  # bottom-left
                (screen_width-1, screen_height-1)  # bottom-right
            ]
            
            corner = random.choice(corners)
            pyautogui.moveTo(corner[0], corner[1], duration=0.2)
            self.log_disruption("Corner Hiding", f"Corner: ({corner[0]},{corner[1]})")
            
        except Exception as e:
            self.log_disruption("ERROR", f"Corner hiding failed: {e}")
            
    def trigger_disruption(self):
        """Trigger a random disruption pattern."""
        if not self.running:
            return
            
        try:
            # Select random disruption pattern
            pattern_name = random.choice(list(self.disruption_patterns.keys()))
            pattern_func = self.disruption_patterns[pattern_name]
            
            # Execute the pattern
            pattern_func()
            
            # For hide/show patterns, restore after duration
            if pattern_name in ['hide_cursor']:
                duration = random.uniform(*self.config['disruption_duration'])
                time.sleep(duration)
                self.show_cursor()
                
        except Exception as e:
            self.log_disruption("ERROR", f"Disruption trigger failed: {e}")
            
    def disruption_loop(self):
        """Main disruption loop that runs in background thread."""
        self.log_disruption("START", "Disruption module activated")
        
        while self.running:
            try:
                # Random interval between disruptions
                interval = random.uniform(*self.config['disruption_interval'])
                time.sleep(interval)
                
                # Probability-based triggering
                if random.random() < self.config['trigger_probability']:
                    self.trigger_disruption()
                    
            except Exception as e:
                self.log_disruption("ERROR", f"Disruption loop error: {e}")
                time.sleep(5)  # Wait before retrying
                
    def start_disruption(self):
        """Start the cursor disruption module."""
        if self.running:
            self.log_disruption("WARNING", "Disruption module already running")
            return
            
        self.running = True
        self.original_position = pyautogui.position()
        
        # Start disruption thread
        self.disruption_thread = threading.Thread(target=self.disruption_loop, daemon=True)
        self.disruption_thread.start()
        
        self.log_disruption("START", f"Disruption module started - Original position: {self.original_position}")
        
    def stop_disruption(self):
        """Stop the cursor disruption module."""
        if not self.running:
            return
            
        self.running = False
        
        # Restore cursor if it was hidden
        try:
            self.show_cursor()
        except:
            pass
            
        # Restore original position
        if self.original_position:
            try:
                pyautogui.moveTo(self.original_position[0], self.original_position[1])
            except:
                pass
                
        self.log_disruption("STOP", "Disruption module stopped")
        
    def keyboard_trigger(self, key_pressed):
        """Trigger disruption based on keyboard input."""
        if key_pressed.lower() in self.config['keyboard_triggers']:
            self.log_disruption("KEYBOARD_TRIGGER", f"Key: {key_pressed}")
            self.trigger_disruption()
            
    def set_config(self, **kwargs):
        """Update configuration parameters."""
        self.config.update(kwargs)
        self.log_disruption("CONFIG", f"Updated: {kwargs}")
        
    def get_status(self):
        """Get current status of the disruption module."""
        return {
            'running': self.running,
            'original_position': self.original_position,
            'current_position': pyautogui.position(),
            'config': self.config.copy()
        }


def main():
    """Demo function to test the cursor disruption module."""
    print("🔧 Cursor Disruption Module Demo")
    print("=" * 40)
    
    # Create disruption module
    disruption = CursorDisruptionModule()
    
    try:
        print("Starting cursor disruption...")
        print("Press Ctrl+C to stop")
        
        # Start disruption
        disruption.start_disruption()
        
        # Keep running
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping cursor disruption...")
        disruption.stop_disruption()
        print("Demo completed!")


if __name__ == "__main__":
    main() 