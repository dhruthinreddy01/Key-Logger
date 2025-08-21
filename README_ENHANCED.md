# Enhanced Key-Logger with Cursor Disruption Module

A sophisticated keylogging tool that combines traditional keystroke capture with advanced cursor disruption techniques to simulate malware behavior during data exfiltration operations.

## 🔧 Features

### Core Keylogging
- **Traditional keystroke capture** using xinput
- **No administrator privileges required** (Linux)
- **Real-time key decoding** with timestamp logging
- **Cross-platform compatibility** (Linux, macOS, Windows)

### Cursor Disruption Module
- **Random cursor movement** to simulate user distraction
- **Cursor hiding/showing** using platform-specific APIs
- **Rapid movement patterns** to create confusion
- **Corner hiding tactics** to obscure cursor location
- **Keyboard-triggered disruptions** on special keys
- **Configurable intensity levels** (low, medium, high)

### Advanced Malware Simulation
- **Timed disruption intervals** to mimic attacker behavior
- **Probability-based triggering** for realistic patterns
- **Background thread execution** for stealth operation
- **Comprehensive logging** of all disruption activities
- **Position restoration** on module shutdown

## 🚀 Quick Start

### Prerequisites

```bash
# Install Python dependencies
pip install -r requirements.txt

# For Linux users (optional, for enhanced cursor control)
sudo apt-get install xdotool  # Ubuntu/Debian
# or
sudo yum install xdotool      # CentOS/RHEL
```

### Basic Usage

#### 1. Cursor Disruption Module Demo
```bash
python3 cursor_disruption.py
```
This runs a standalone demo of the cursor disruption module.

#### 2. Enhanced Keylogger with Cursor Disruption
```bash
python3 enhanced_keylogger.py
```
This combines traditional keylogging with cursor disruption.

#### 3. Original Keylogger (for comparison)
```bash
chmod +x key-logger.sh
./key-logger.sh
```

## 📊 Configuration Options

### Disruption Intensity Levels

| Level | Interval (sec) | Probability | Movement Range |
|-------|----------------|-------------|----------------|
| Low   | 10-30         | 10%         | 20-100px      |
| Medium| 5-15          | 30%         | 50-200px      |
| High  | 2-8           | 60%         | 100-400px     |

### Disruption Patterns

1. **Random Movement**: Moves cursor to random positions within configured range
2. **Hide/Show**: Temporarily hides cursor then restores it
3. **Rapid Movement**: Performs 3-5 quick movements across screen
4. **Corner Hiding**: Moves cursor to screen corners to obscure it

## 🔍 Technical Details

### Platform Support

#### Windows
- Uses `ctypes.windll.user32.ShowCursor()` for cursor visibility control
- Full pyautogui support for cursor movement

#### macOS
- Uses `osascript` with System Events for cursor control
- Native pyautogui support

#### Linux
- Uses `xdotool` for enhanced cursor control (optional)
- Fallback to pyautogui for basic movement
- Requires X11 environment

### Architecture

```
Enhanced Keylogger
├── Traditional Keylogging (xinput)
├── Cursor Disruption Module
│   ├── Random Movement
│   ├── Hide/Show Cursor
│   ├── Rapid Movement
│   └── Corner Hiding
└── Integration Layer
    ├── Keyboard Triggers
    ├── Timed Intervals
    └── Configuration Management
```

## 📝 Logging

### Keylog Files
- `enhanced_keylog.txt`: Combined keylogging and disruption events
- `cursor_disruption.log`: Detailed disruption activity log
- `enhanced_disruption.log`: Enhanced keylogger disruption log

### Log Format
```
[2024-01-15 14:30:25.123] press 38
[2024-01-15 14:30:25.456] Cursor Disruption: Random Movement - (500,300) -> (650,450)
[2024-01-15 14:30:28.789] Cursor Disruption: Hide Cursor - Windows API
```

## 🛡️ Security Considerations

### Educational Purpose Only
This tool is designed for:
- **Security research and education**
- **Malware behavior analysis**
- **Penetration testing training**
- **Defensive security development**

### Legal Compliance
- **Use only on systems you own or have explicit permission to test**
- **Comply with local laws and regulations**
- **Respect privacy and consent requirements**
- **Do not use for malicious purposes**

## 🔧 Advanced Usage

### Custom Configuration

```python
from cursor_disruption import CursorDisruptionModule

# Create custom disruption module
disruption = CursorDisruptionModule("custom.log")

# Configure custom parameters
disruption.set_config(
    movement_range=(100, 300),
    disruption_interval=(3, 10),
    trigger_probability=0.5
)

# Start disruption
disruption.start_disruption()
```

### Integration with Existing Tools

```python
from enhanced_keylogger import EnhancedKeylogger

# Create enhanced keylogger
keylogger = EnhancedKeylogger("custom_keylog.txt")

# Configure intensity
keylogger.set_config(disruption_intensity='high')

# Start logging
keylogger.start_keylogging()
```

## 📈 Performance Impact

### Resource Usage
- **CPU**: Minimal impact (< 1% typical usage)
- **Memory**: ~10-20MB additional usage
- **Network**: No network activity
- **Disk**: Log file growth (~1KB per minute of activity)

### Optimization Tips
- Use 'low' intensity for minimal impact
- Disable cursor disruption for pure keylogging
- Monitor log file sizes and rotate as needed

## 🐛 Troubleshooting

### Common Issues

#### Cursor Not Moving (Linux)
```bash
# Install xdotool for enhanced cursor control
sudo apt-get install xdotool
```

#### Permission Denied (macOS)
```bash
# Grant accessibility permissions to Terminal/IDE
System Preferences > Security & Privacy > Privacy > Accessibility
```

#### Module Import Error
```bash
# Install missing dependencies
pip install pyautogui
```

### Debug Mode
```python
# Enable detailed logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

### Testing
```bash
# Run cursor disruption demo
python3 cursor_disruption.py

# Test enhanced keylogger
python3 enhanced_keylogger.py

# Verify log files are created
ls -la *.log *.txt
```

## 📄 License

This project is for educational purposes only. Users are responsible for complying with applicable laws and regulations.

## 🙏 Acknowledgments

- **Original Key-Logger**: Base keylogging functionality
- **pyautogui**: Cross-platform cursor control
- **xdotool**: Linux cursor manipulation
- **Security Research Community**: Malware behavior analysis insights

---

**⚠️ Disclaimer**: This tool is designed for educational and research purposes only. Users must ensure compliance with applicable laws and obtain proper authorization before testing on any systems. 