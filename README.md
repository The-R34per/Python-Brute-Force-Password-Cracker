# Python-Brute-Force-Password-Cracker
=====================

A pure Python brute-force password cracker for educational cybersecurity demos. 
Uses itertools.product to test all printable ASCII combinations while tracking 
precise timing and attempt counts. Demonstrates why strong passwords matter.

# BADGES:
[Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)
[License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

# USAGE
-----
Input the password to crack: test
Password cracked in 1046 attempts (0.02 seconds).
Your password was: test

# FEATURES:
--------
- Exhaustive brute-force (94 printable chars)
- time.perf_counter() for sub-ms precision 
- Real-time attempt counter
- Early exit on match
- Clean console output

# PERFORMANCE
-----------
Password | Attempts    | Time
---------|-------------|------
ab       | 1,046       | 0.00s
easy     | 12,558,717  | ~3 seconds
pass     | 21,695,135  | ~6 seconds
Password | 66 trillion | ~2 years

# EDUCATIONAL USE ONLY
--------------------
✅ Test YOUR weak passwords
✅ Classroom demos
✅ Security presentations
❌ Production systems
❌ Unauthorized access

# WHY IT MATTERS
--------------
- 8 char passwords crack in days with real tools
- 12+ random chars = practically uncrackable
- Always use 2FA + password manager


# LICENSE: 
Python Brute Force Password Cracker © 2025 by The-R34per is licensed under CC BY-SA 4.0. To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0/
