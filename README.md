# Setting Up Google Cloud Platform (GCP) Credentials and Running a Python Script to Send Emails

This guide will walk you through the steps to set up credentials on Google Cloud Platform (GCP), configure the consent screen, and run a Python script to send emails using the Gmail API.

## Prerequisites

- Python installed on your system (version 3.6 or higher recommended).
- Basic understanding of Python and working with terminal or command prompt.
- Access to a Google account.

## Steps

### 1. Create a New Project on Google Cloud Platform

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing project from the project selector at the top of the page.
   - **Project Name**: `gmailApi`
   - **Owner**: `saranguber7@gmail.com` (your Google account)

### 2. Enable the Gmail API

1. In the Cloud Console, navigate to `APIs & Services` > `Library`.
2. Search for "Gmail API" and click on it.
3. Click `Enable` to enable the Gmail API for your project.

### 3. Set Up OAuth Consent Screen

1. In the Cloud Console, navigate to `APIs & Services` > `OAuth consent screen`.
2. Choose `External` user type (since you are including external email addresses).
3. Fill in the required fields:
   - **App Information**:
     - **User support email**: `sarangjoshi.g@gmail.com`
   - **Scopes for Google APIs**:
     - Click `Add or remove scopes` and add the following scope:
       - `https://www.googleapis.com/auth/gmail.send`: Allows sending emails on behalf of the user.
   - **Test users**:
     - Add your Google account email address for testing purposes: `saranguber7@gmail.com`
     - Add any additional email addresses (e.g., `sarangjoshi.g@gmail.com`) for testing.
   - **Authorized domains** (optional):
     - Add domains if your app is intended to work only with specific domains.
   - **App Homepage link** (optional):
     - Provide a link to the homepage of your app.
   - **Application Privacy Policy link** (optional):
     - Provide a link to your privacy policy.
4. Click `Save and Continue`.

### 4. Create OAuth 2.0 Credentials

1. In the Cloud Console, navigate to `APIs & Services` > `Credentials`.
2. Click `Create Credentials` and select `OAuth client ID`.
3. Choose `Desktop app` as the application type.
4. Provide a name for your OAuth client (e.g., "Gmail API Client").
5. Click `Create`. This will download a `credentials.json` file. **Keep this file safe as it contains your client ID and client secret.**

### 5. Prepare Your Python Environment

1. Create a new directory for your project.
2. Place the `credentials.json` file you downloaded from GCP into this directory.
3. Create a new Python script (e.g., `send_email.py`) in the same directory.

### 6. Install Required Python Packages

1. Open a terminal or command prompt.
2. Navigate to your project directory.
3. Create a virtual environment (optional but recommended):
   ```sh
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
