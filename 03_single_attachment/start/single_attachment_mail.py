import smtplib
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define your SMTP server details from environment variables
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_SERVER_PORT = os.getenv("SMTP_SERVER_PORT")

# Define your sender email address and password from environment variables
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")
SENDER_EMAIL_PASSWORD = os.getenv("SENDER_EMAIL_PASSWORD")

# Define the receiver email address from environment variables
RECEIVER_EMAIL_ADDRESS = os.getenv("RECEIVER_EMAIL_ADDRESS")

# Define your subject and body for the email
subject = "Meeting Reminder: Project Update"
body = """
Dear Students,

This is a reminder about our upcoming project update meeting scheduled for tomorrow at 10:00 AM. 
Please ensure that you have your progress reports ready and be prepared to discuss any blockers you are facing.

Looking forward to your participation.

Best regards,
Susheel Thapa
"""

# Construct the email message
message = f'Subject: {subject}\n\n{body}'

print("Initializing SMTP server connection...")

# Initialize the SMTP server connection
smtp = smtplib.SMTP(SMTP_SERVER, int(SMTP_SERVER_PORT))
print("SMTP server connection initialized.")

print("Starting TLS encryption...")
# Start TLS encryption
smtp.starttls()
print("TLS encryption started.")

print("Logging in to the SMTP server...")
# Login to the SMTP server
smtp.login(SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD)
print("Logged in to the SMTP server.")

print("Sending the email...")
# Send the email
smtp.sendmail(SENDER_EMAIL_ADDRESS, RECEIVER_EMAIL_ADDRESS, message)
print("Email sent successfully!")

print("Closing the SMTP server connection...")
# Close the SMTP server connection
smtp.quit()
print("SMTP server connection closed.")
