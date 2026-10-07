CYBERSECURITY OSINT AUTOMATED DATA COLLECTION PROJECT

Student: Rati Abulashvili
Professor: Stoney Walker
ITSY 1307-20001
10.7.2026

PROJECT DESCRIPTION

This project is a Python-based cybersecurity OSINT automation tool.
The program collects publicly available cybersecurity information
from a public RSS feed and stores the results in JSON format.

FILES

cybersecurity_osint.py
Main Python automation script.

cybersecurity_news.json
JSON file containing the collected cybersecurity information.

README.txt
Project documentation.

report.pdf
Final assignment report.

REQUIREMENTS

Python 3
Requests library

INSTALLATION

Install Python and the Requests library:

python -m pip install requests

RUNNING THE PROGRAM

Open Command Prompt in the project directory and run:

python cybersecurity_osint.py

The program connects to a public cybersecurity information source,
collects cybersecurity article information, displays the results,
and saves the information to cybersecurity_news.json.

ETHICAL CONSIDERATIONS

The program collects publicly available information only. It does
not attempt to access private accounts, bypass authentication,
collect personal information, or exploit systems.

The purpose of the project is educational and defensive. Automated
data collection should always respect applicable laws, website
policies, privacy requirements, and reasonable access limits.