import os.path
import base64
import google.auth
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import os
from os.path import join, dirname, realpath
from google_auth_oauthlib.flow import InstalledAppFlow

# Assuming SCOPES is defined elsewhere in your script
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate():
    # Get the path to the parent directory of 'oauth_gmail'
    current_dir = dirname(realpath(__file__))
    parent_dir = realpath(join(current_dir, '..'))
    
    # Path to credentials.json relative to the parent directory
    credentials_path = join(parent_dir, 'credentials.json')

    flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
    creds = flow.run_local_server(port=0)

    return creds


# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def authenticate():
    # Get the path to the parent directory of 'oauth_gmail'
    current_dir = dirname(realpath(__file__))
    parent_dir = realpath(join(current_dir, '..'))

    # Path to credentials.json relative to the parent directory
    credentials_path = join(parent_dir, 'credentials.json')
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Provide the correct path to your credentials.json file
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            flow.redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
            auth_url, _ = flow.authorization_url(prompt='consent')
            print(f"Please go to this URL: {auth_url}")
            code = input("Enter the authorization code: ")
            flow.fetch_token(code=code)
            creds = flow.credentials
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def send_email(service, sender_email, recipient_email, subject, body):
    message = MIMEText(body)
    message['to'] = recipient_email
    message['from'] = sender_email
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    message = {'raw': raw_message}

    try:
        message = (service.users().messages().send(userId="me", body=message).execute())
        print(f'Message Id: {message["id"]}')
        return message
    except Exception as e:
        print(f'An error occurred: {e}')
        return None

def main():
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)

    sender_email = 'sarangjoshi.g@gmail.com'
    recipient_email = 'bshreyas13@gmail.com'
    subject = 'Test Email'
    body = 'This is a test email sent from a Python script using OAuth 2.0.'

    send_email(service, sender_email, recipient_email, subject, body)

if __name__ == '__main__':
    main()
