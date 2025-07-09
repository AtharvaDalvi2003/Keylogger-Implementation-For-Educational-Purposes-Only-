🛡️ Keylogger Implementation (For Educational Purposes Only)
---
⚠️ **Disclaimer:** This project is intended strictly for ethical, educational, and research purposes only. Do not use this tool for malicious activity. Unauthorized use of a keylogger may violate privacy laws and result in criminal charges.

---

## 🎯 Objective

To understand the basic working of a keylogger by building a simple Python-based implementation that:
- Logs keystrokes to a local file
- Demonstrates how keyloggers work
- Raises awareness to help develop better cybersecurity defenses

---

## 🛠️ Technologies Used

- **Python 3**
- **pynput** – For capturing keyboard input
- **File I/O** – For storing keystrokes in a text log

---

## 📦 Requirements

Before running the script, install the required Python library:

```bash
pip install pynput
```
---
## 🔍 Features
- ⌨️ Captures every keystroke typed on the keyboard

- 📁 Logs all input to a local .txt file

- 🧪 Lightweight and easy to understand for ethical testing

- 🔐 Demonstrates vulnerabilities in systems lacking input monitoring protections
```
```
---
## 📁 Project Structure
```
keylogger-educational/
│
├── keylogger.py           # Main keylogger script
├── keystrokes.txt         # Output log file (auto-created)
└── README.md
```
---
## 🚀 How to Run
1. Clone the repository
```
git clone https://github.com/AtharvaDalvi2003/keylogger-educational.git
cd keylogger-educational
```
2. Run the keylogger script
```
python keylogger.py
```
3.Check the output
- All keystrokes will be saved in keystrokes.txt in the same directory.
---
## ✅ Expected Outcome
- A working keylogger script for educational use only

- Helps in understanding:

- How keystrokes can be captured

- Why protecting input and system access is critical

- How endpoint security software should detect keyloggers
  
- The keylogger works silently in the background.
  
- All keystrokes typed are logged in `keystrokes.txt`.
  
- Open this file to see the captured inputs.
  
- No terminal output is shown during execution.

### 📸 Example Log Output (Optional Screenshot Below)
<img width="1916" height="1017" alt="Image" src="https://github.com/user-attachments/assets/aa3871fe-7abd-467d-a0e5-276e0a0f57cf" />

- 🔐 Educational Purpose Only – Use Responsibly.
---
## 📜 License
This project is open-source and available under the MIT License.
