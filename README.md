# OTP-Console-Based
🔐 OTP Verification System (Python)
This Python script generates and sends a One-Time Password (OTP) via email to authenticate users. It provides a secure and automated way to verify user identity using an email-based OTP system.

📌 Features
✅ Random OTP Generation – Generates a secure 4-digit OTP for authentication.
✅ Email-Based OTP Delivery – Sends OTP via Gmail SMTP using a secure connection.
✅ User Authentication – Requires the recipient to enter the correct OTP to verify their identity.
✅ Limited Attempts – Users have 3 chances to enter the correct OTP before verification fails.
✅ Secure Email Transmission – Uses TLS encryption for safe communication.
✅ Multi-User Support – Allows sending OTPs to multiple users in a single execution.
✅ Customizable OTP Length – Modify the script to generate 6-digit OTPs for stronger security.
✅ Error Handling – Proper exception handling for invalid inputs and email delivery failures.
✅ Future Expansion – Can be integrated into web applications or login systems.

⚙️ How It Works
The script prompts the user for their name and email address.
A random OTP (4-digit number) is generated.
The OTP is sent to the provided email using Gmail SMTP.
The user is prompted to enter the received OTP.
If the OTP matches, verification succeeds.
If the user enters the wrong OTP, they get 3 attempts before the verification fails.

🛠 Prerequisites
Before running the script, ensure you have:
1️⃣ Python Installed (3.x recommended)
Download and install Python from the official website: Python.org
2️⃣ A Gmail Account with App Passwords Enabled
Since Google no longer allows less secure apps to access Gmail SMTP, you need to generate an App Password:
Go to Google Account Settings → Security → App Passwords
Select Mail and Your Device to generate a password
Use this generated password instead of your actual Gmail password in the script
3️⃣ Required Python Libraries
Install dependencies using pip (if not already installed):
bash
Copy
Edit
pip install smtplib email
🚀 How to Run the Script
Open a terminal or command prompt.

Run the Python script:
bash
Copy
Edit
python otp_verification.py
Enter the required details when prompted:
Your name
Recipient's email address
Check the recipient’s email for the OTP.
Enter the received OTP in the terminal.
If the OTP is correct, you’ll see: "OTP Verification Success"
If incorrect, you’ll have 3 attempts before failure.

🔒 Security Considerations
🔹 Use Environment Variables: Instead of hardcoding credentials, store your Gmail email and App Password in environment variables.
🔹 Enable App Passwords for Gmail: Avoid using your actual Gmail password in the script.
🔹 Limit OTP Attempts: The script already provides 3 attempts for added security.
🔹 Avoid Sending OTPs in Plain Text: Consider encrypting the OTP before sending for enhanced security.
🔹 Use a More Secure OTP Length: Instead of 4-digit OTPs, you can increase the OTP length (e.g., 6 digits).

🔧 Future Enhancements
💡 Use a Secure Database: Store OTPs in a secure database instead of handling them in memory.
💡 Enhance Logging: Implement logging to track OTP requests and attempts.
💡 Add SMS Support: Integrate Twilio or Firebase for SMS OTP verification.
💡 Web Integration: Convert this script into a Flask/Django API for web-based OTP authentication.
💡 Multi-Factor Authentication (MFA): Use OTP as part of a larger MFA system.

