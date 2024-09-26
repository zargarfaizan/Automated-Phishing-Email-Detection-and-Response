# Automated-Phishing-Email-Detection-and-Response

This project automates the detection of phishing emails using heuristic methods and VirusTotal API. It automatically quarantines emails, alerts the security team, and logs incidents.

#Requirements
Flask
imaplib
requests
sqlite3
smtplib
email
unittest


## Features:
- Email fetching via IMAP
- Phishing detection based on keywords and malicious URLs
- Automated responses (quarantine, alerts)
- Incident logging to SQLite
- Optional Flask web app to view incidents

## Setup:
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Replace the placeholder values for email credentials and VirusTotal API in the code.
4. Run the phishing detection script: `python src/email_fetcher.py`.
5. Optionally, start the Flask app: `python src/flask_app.py`.

## Future Enhancements:
- More advanced phishing detection heuristics.
- Integrate with other threat intelligence APIs.
- Add more sophisticated email parsing.
