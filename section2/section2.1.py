import os
import base64

from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from email.message import EmailMessage
from googleapiclient import errors
import configparser

class GmailUtils:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        self.service = self.gmail_authenticate()
        
    def gmail_authenticate(self):
        SCOPES = ["https://mail.google.com/"]
        creds = None
        
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                client_secret_path = self.config.get("credential", "client_secrets")
                flow = InstalledAppFlow.from_client_secrets_file('./private/credential.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        return build("gmail", "v1", credentials=creds)

    def create_message(self, sender, to, subject, message_text, content_type = 'html'):
        message = EmailMessage()
        message.set_content(message_text, subtype=content_type)
        bcc_emails = self.config.get("Bcc", "bcc")
        message["From"] = sender
        message["To"] = to.split(",")
        message['bcc'] = bcc_emails
        message["subject"] = subject

        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode('utf8','surrogateescape')}

    def send_message(self, user_id, message):
        try:
            message = self.service.users().messages().send(userId=user_id, body=message).execute()
            print('Message Id: %s' % message['id'])
            return message
        
        except errors.HttpError as error:
            print('An error occurred: %s' % error)

def load_template(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    gmail = GmailUtils()

    config = configparser.ConfigParser()
    config.read('config.ini')
    sender = config.get("Sender", "sender")

    to = "mia.p@knworks.co.kr" # 받는 사람
    subject = "Hello world!" # 이메일 제목
    # message_text = "Hello, this is a test email." # 이메일 본문
    message_text = load_template('./templates/section2_mail_template.html')
    message = gmail.create_message(sender, to, subject, message_text)
    gmail.send_message("me", message)

if __name__ == "__main__":
    main()
