# Python Log Analyzer

A beginner cybersecurity project built with Python that analyzes login activity from log files and detects suspicious behavior such as repeated failed logins and rapid login attempts.

## Features

* Reads and parses log files line-by-line
* Detects `LOGIN_FAILED` events
* Tracks failed login counts
* Extracts timestamps using regex
* Calculates time differences between login attempts
* Detects rapid failed login activity
* Extracts IP addresses dynamically using regex
* Tracks failed login attempts by IP address using dictionaries

---

# Technologies Used

* Python 3
* Regular Expressions (`re`)
* Datetime handling (`datetime`)
* Git + GitHub
* Ubuntu WSL
* VS Code

---

# Example Log Format

```txt
2026-05-12 08:22:44 LOGIN_FAILED user=admin ip=10.0.0.8
2026-05-12 08:23:01 LOGIN_FAILED user=admin ip=10.0.0.8
2026-05-12 08:23:19 LOGIN_FAILED user=admin ip=10.0.0.8
```

---

# Current Detection Logic

The program currently:

1. Reads each log line
2. Extracts timestamps using regex
3. Converts timestamps into Python datetime objects
4. Calculates the time difference between login attempts
5. Resets counters when login attempts are too far apart
6. Detects repeated failed logins in short time windows
7. Tracks failed attempts per IP address

---

# Example Output

```txt
LOGIN FAIL
Current Count 1

LOGIN FAIL
Current Count 2

LOGIN FAIL
Current Count 3
Suspicious Activity Detected
```

---

# Skills Learned

This project helped practice:

* Python programming fundamentals
* File handling
* Loops and conditionals
* Dictionaries
* Regex pattern matching
* Datetime calculations
* Linux terminal usage
* Git version control
* Basic cybersecurity detection logic

---

# Future Improvements

Planned upgrades:

* Generate full security reports
* Export findings to report files
* Track failed attempts by username
* Detect failed logins followed by successful logins
* Build a Flask web dashboard
* Add live monitoring capabilities
* Add data visualizations and charts

---

# Running the Project

```bash
python3 main.py
```

---

# Author

Frank Ragauskis
