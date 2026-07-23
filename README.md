# Password Strength Auditor

**In simple terms:** this tool looks at a password and tells you whether it's weak or strong, like a security guard checking IDs at a door. It checks how long the password is and whether it mixes letters, numbers, and symbols.

A Python command-line tool that audits password strength. It checks length and character variety (uppercase, lowercase, numbers, symbols), then scores the password 0-5 and gives a verdict: WEAK, DECENT, or STRONG.

![Demo](Screenshot%202026-07-21%20at%2011.05.55.png)
*Above: the tool running in a terminal. The user enters a password, and the program shows its length, a score out of 5, and a final verdict.*

Built as a hands-on learning project while transitioning from physical security into cybersecurity. 

## Why this matters
Weak passwords are one of the most common ways accounts get hacked. This tool applies the same length and complexity guidelines used by real security standards (NIST) to help someone quickly judge if their password is safe.

## How it works
- Enter a password (or type 'quit' to exit)
- The tool checks length and character types
- It calculates a score out of 5
- It returns a verdict based on the score

## Run it
```
python3 auditor.py
```
