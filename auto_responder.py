import smtplib
from email.mime.text import MIMEText
from incident_logger import log_incident

# Automatically respond to phishing emails
def respond_to_phishing(subject):
    # Quarantine or alert action (placeholder)
    log_incident(subject)

    # Send an alert email to security team
    send_alert_email(subject)

# Function to send an alert
def send_alert_email(subject):
    sender_email = "your_email@gmail.com"
    receiver_email = "security_team@example.com"
    msg = MIMEText(f"Phishing email detected with subject: {subject}")
    msg['Subject'] = "Phishing Alert"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, "your_password")
        server.sendmail(sender_email, receiver_email, msg.as_string())
