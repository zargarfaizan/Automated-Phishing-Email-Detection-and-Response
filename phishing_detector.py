import re
import requests

# Simple phishing detection based on heuristic rules
def check_phishing(email_obj):
    subject = email_obj["subject"]
    email_body = get_email_body(email_obj["email_obj"])

    phishing_keywords = ["password", "urgent", "login", "verify", "click"]
    is_phishing = any(keyword in email_body.lower() for keyword in phishing_keywords)

    urls = extract_urls(email_body)
    is_malicious_url = any(check_url(url) for url in urls)

    return is_phishing or is_malicious_url

# Function to extract body content from the email
def get_email_body(email_obj):
    if email_obj.is_multipart():
        for part in email_obj.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode()
    return email_obj.get_payload(decode=True).decode()

# Function to extract URLs from email
def extract_urls(text):
    urls = re.findall(r'(https?://\S+)', text)
    return urls

# Function to check if URL is malicious using VirusTotal API
def check_url(url):
    api_key = "YOUR_VIRUSTOTAL_API_KEY"
    params = {'apikey': api_key, 'resource': url}
    response = requests.get('https://www.virustotal.com/vtapi/v2/url/report', params=params)
    result = response.json()
    return result['positives'] > 0 if 'positives' in result else False
