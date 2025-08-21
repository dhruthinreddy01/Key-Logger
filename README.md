# Key-Logger
A simple program that helps you log your keystrokes.  

Key-Logger doesn't require *administrator* access to log keys. Also it has no dependencies on external libraries, unlike other programs that require *administrator access* even to install them.

## 🔧 Enhanced Version Available

This repository now includes an **Enhanced Keylogger with Cursor Disruption Module** that simulates advanced malware behavior:

- **Traditional keylogging** with timestamp logging
- **Cursor disruption simulation** using pyautogui
- **Platform-specific cursor control** (Windows, macOS, Linux)
- **Configurable disruption intensity** (low, medium, high)
- **Keyboard-triggered disruptions** on special keys
- **Comprehensive logging** of all activities

### Enhanced Features
- **Random cursor movement** to simulate user distraction
- **Cursor hiding/showing** using platform-specific APIs
- **Rapid movement patterns** to create confusion
- **Corner hiding tactics** to obscure cursor location
- **Background thread execution** for stealth operation

### Quick Start (Enhanced Version)
```bash
# Install dependencies
pip install -r requirements.txt

# Run cursor disruption demo
python3 cursor_disruption.py

# Run enhanced keylogger
python3 enhanced_keylogger.py

# Test functionality
python3 test_cursor_disruption.py
```

For detailed documentation, see [README_ENHANCED.md](README_ENHANCED.md).

---

###### Note: Original version supports only Linux. Enhanced version supports Windows, macOS, and Linux.

### Requirements

**Original Version**: No special requirements except **Python3**.

**Enhanced Version**: See `requirements.txt` for dependencies.

### Usage (Original Version)
**Add key-logger as executable**

    chmod +x key-logger.sh

**Start logging**

    ./key-logger.sh

Select the **keyboard ID** from the list shown, which you want to log.

**Parse key-log**

    python3 parser.py <log_file>