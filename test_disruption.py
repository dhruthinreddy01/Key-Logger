#!/usr/bin/env python3
"""
Test script for Cursor Disruption Module
Verifies functionality and provides a safe testing environment.
"""

import sys
import time
import os

def test_imports():
    """Test if all required modules can be imported."""
    print("🔍 Testing imports...")
    
    try:
        import pyautogui
        print("✅ pyautogui imported successfully")
    except ImportError as e:
        print(f"❌ pyautogui import failed: {e}")
        return False
        
    try:
        import threading
        import time
        import random
        print("✅ Standard library modules imported successfully")
    except ImportError as e:
        print(f"❌ Standard library import failed: {e}")
        return False
        
    try:
        if sys.platform == "win32":
            import ctypes
            print("✅ Windows ctypes imported successfully")
        elif sys.platform == "darwin":
            import subprocess
            print("✅ macOS subprocess imported successfully")
        elif sys.platform.startswith("linux"):
            import subprocess
            print("✅ Linux subprocess imported successfully")
    except ImportError as e:
        print(f"⚠️  Platform-specific import warning: {e}")
        
    return True

def test_cursor_disruption_module():
    """Test the cursor disruption module."""
    print("\n🔧 Testing Cursor Disruption Module...")
    
    try:
        from cursor_disruption import CursorDisruptionModule
        print("✅ CursorDisruptionModule imported successfully")
        
        # Create instance
        disruption = CursorDisruptionModule("test_disruption.log")
        print("✅ CursorDisruptionModule instance created")
        
        # Test configuration
        disruption.set_config(disruption_interval=(1, 2), trigger_probability=1.0)
        print("✅ Configuration updated successfully")
        
        # Test status
        status = disruption.get_status()
        print(f"✅ Status retrieved: {status['running']}")
        
        return True
        
    except Exception as e:
        print(f"❌ CursorDisruptionModule test failed: {e}")
        return False

def test_enhanced_keylogger():
    """Test the enhanced keylogger module."""
    print("\n🔍 Testing Enhanced Keylogger...")
    
    try:
        from enhanced_keylogger import EnhancedKeylogger
        print("✅ EnhancedKeylogger imported successfully")
        
        # Create instance
        keylogger = EnhancedKeylogger("test_keylog.txt")
        print("✅ EnhancedKeylogger instance created")
        
        # Test configuration
        keylogger.set_config(disruption_intensity='low')
        print("✅ Configuration updated successfully")
        
        # Test status
        status = keylogger.get_status()
        print(f"✅ Status retrieved: {status['running']}")
        
        return True
        
    except Exception as e:
        print(f"❌ EnhancedKeylogger test failed: {e}")
        return False

def test_pyautogui_functionality():
    """Test basic pyautogui functionality."""
    print("\n🖱️  Testing pyautogui functionality...")
    
    try:
        import pyautogui
        
        # Get screen size
        screen_size = pyautogui.size()
        print(f"✅ Screen size detected: {screen_size}")
        
        # Get current position
        current_pos = pyautogui.position()
        print(f"✅ Current cursor position: {current_pos}")
        
        # Test small movement (safe)
        original_pos = current_pos
        pyautogui.moveRel(10, 10, duration=0.1)
        time.sleep(0.2)
        pyautogui.moveRel(-10, -10, duration=0.1)
        
        # Verify position restored
        final_pos = pyautogui.position()
        if abs(final_pos[0] - original_pos[0]) < 5 and abs(final_pos[1] - original_pos[1]) < 5:
            print("✅ Cursor movement test passed")
        else:
            print("⚠️  Cursor position may have changed slightly")
            
        return True
        
    except Exception as e:
        print(f"❌ pyautogui test failed: {e}")
        return False

def test_platform_specific_features():
    """Test platform-specific cursor control features."""
    print(f"\n🖥️  Testing platform-specific features ({sys.platform})...")
    
    try:
        if sys.platform == "win32":
            import ctypes
            # Test Windows cursor control (just check if available)
            print("✅ Windows ctypes cursor control available")
            
        elif sys.platform == "darwin":
            import subprocess
            # Test macOS cursor control
            result = subprocess.run(['osascript', '-e', 'tell application "System Events" to get name of first process'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ macOS System Events available")
            else:
                print("⚠️  macOS System Events may require permissions")
                
        elif sys.platform.startswith("linux"):
            import subprocess
            # Test Linux xdotool availability
            result = subprocess.run(['which', 'xdotool'], capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ xdotool available on Linux")
            else:
                print("⚠️  xdotool not installed (optional for enhanced features)")
                
        return True
        
    except Exception as e:
        print(f"❌ Platform-specific test failed: {e}")
        return False

def run_demo_test():
    """Run a brief demo test of the cursor disruption."""
    print("\n🎬 Running brief demo test...")
    
    try:
        from cursor_disruption import CursorDisruptionModule
        
        # Create disruption module with very short intervals for testing
        disruption = CursorDisruptionModule("demo_test.log")
        disruption.set_config(
            disruption_interval=(1, 2),
            trigger_probability=1.0,
            movement_range=(10, 50)
        )
        
        print("Starting 5-second demo...")
        disruption.start_disruption()
        
        # Run for 5 seconds
        time.sleep(5)
        
        disruption.stop_disruption()
        print("✅ Demo test completed successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Demo test failed: {e}")
        return False

def main():
    """Main test function."""
    print("🧪 Cursor Disruption Module Test Suite")
    print("=" * 50)
    
    tests = [
        ("Import Test", test_imports),
        ("Cursor Disruption Module", test_cursor_disruption_module),
        ("Enhanced Keylogger", test_enhanced_keylogger),
        ("pyautogui Functionality", test_pyautogui_functionality),
        ("Platform-Specific Features", test_platform_specific_features),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        if test_func():
            passed += 1
            print(f"✅ {test_name} PASSED")
        else:
            print(f"❌ {test_name} FAILED")
            
    print(f"\n{'='*50}")
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The cursor disruption module is ready to use.")
        
        # Ask if user wants to run demo
        response = input("\nWould you like to run a 5-second demo? (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            run_demo_test()
    else:
        print("⚠️  Some tests failed. Please check the error messages above.")
        
    print("\n📝 Next steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Run cursor disruption demo: python3 cursor_disruption.py")
    print("3. Run enhanced keylogger: python3 enhanced_keylogger.py")

if __name__ == "__main__":
    main() 