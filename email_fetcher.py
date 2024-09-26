import imaplib
import email
from email.header import decode_header

# Email fetcher to connect to an email server and pull emails
def fetch_emails(username, password, imap_server):
    # Connect to the email server
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(username, password)

    # Select the inbox
    mail.select("inbox")

    # Search for all emails
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()

    emails = []
    
    for email_id in email_ids[-5:]:  # Fetching the last 5 emails
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                emails.append({"subject": subject, "email_obj": msg})

    mail.logout()
    return emails
