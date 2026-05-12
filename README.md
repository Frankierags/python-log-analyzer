# Python Security Log Analyzer

A Python-based cybersecurity log analysis tool that simulates authentication events, detects suspicious login behavior, and generates automated security reports.

## Features

- Parses simulated authentication logs
- Detects failed login attempts
- Identifies brute-force attack patterns
- Tracks suspicious IP addresses
- Generates automated security reports
- Simulates realistic login events using a log generator
- Tracks multiple security event types
- Assigns severity levels based on detected activity

---

# Technologies Used

- Python 3
- Regex (`re`)
- Datetime module
- File handling
- Dictionaries / event tracking
- Linux terminal environment

---

# Project Structure

```text
python-log-analyzer/
│
├── main.py
├── log_generator.py
├── sample_logs.txt
├── report.txt
└── README.md
```

---

# How It Works

## 1. Log Generator

`log_generator.py` simulates authentication activity by generating fake log events such as:

- LOGIN_SUCCESS
- LOGIN_FAILED
- UNKNOWN_USER
- ACCOUNT_LOCKED

Example generated logs:

```text
2026-05-12 15:53:27 LOGIN_FAILED 61.124.247.191
2026-05-12 15:53:27 LOGIN_SUCCESS 172.98.109.21
2026-05-12 15:53:29 ACCOUNT_LOCKED 192.213.81.145
```

---

## 2. Log Analyzer

`main.py` parses the logs and performs analysis including:

- Counting failed login attempts
- Tracking suspicious IP addresses
- Detecting brute-force activity
- Tracking event frequencies
- Assigning severity levels
- Generating automated security recommendations

---

# Example Report Output

```text
=== Security REPORT ===

REPORT GENERATED AT: 2026-05-12 15:53:44

== EVENT SUMMARY ==
LOGIN_FAILED       | Count: 19
UNKNOWN_USER       | Count: 2
LOGIN_SUCCESS      | Count: 3
ACCOUNT_LOCKED     | Count: 1

FAILED LOGIN ATTEMPTS: 19
BRUTE FORCE ALERTS: 3
SEVERITY LEVEL: HIGH

ATTACK TYPES DETECTED: Brute Force

== Suspicious IPS ==
61.124.247.191     | Failed Attempts: 7
151.146.21.25      | Failed Attempts: 4
174.164.194.125    | Failed Attempts: 7

=== RECOMMENDED ACTION ===

- Investigate repeated failed logins immediately.
- Consider temporarily blocking high-risk IPs.
- Review account activity for compromise.
```

---

# Running The Project

## Generate Logs

```bash
python3 log_generator.py
```

## Analyze Logs

```bash
python3 main.py
```

## View Report

```bash
cat report.txt
```

---

# Skills Demonstrated

- Cybersecurity event analysis
- Log parsing
- Regex pattern matching
- Threat detection logic
- Security reporting automation
- Python scripting
- Linux command-line workflow
- Event correlation
- Basic SIEM-style analysis concepts

---

# Future Improvements

- Username-based attack detection
- Password spraying detection
- CSV export support
- Real-time log monitoring
- IP reputation lookup
- Dashboard visualization
- GeoIP analysis
- Multi-system log support
- JSON log parsing
- Alert prioritization

---

# Author

Frank Ragauskis  
Cybersecurity / Computer Science Student at Iowa State University