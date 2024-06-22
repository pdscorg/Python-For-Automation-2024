import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
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

# Define the subject for the email
subject = "PDSC Python for Automation Workshop - Certificate of Participation"


def send_email(receiver_email):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = SENDER_EMAIL_ADDRESS
    message["To"] = receiver_email

    # Add body content (plain text)
    body = """Dear Participant,

    Thank you for participating in the PDSC Python for Automation workshop!

    Attached to this email, you will find your certificate of participation.

    We hope you found the workshop informative and valuable. Should you have any questions or feedback, feel free to reach out to us.

    Best regards,
    PDSC Team
    """
    message.attach(MIMEText(body, "plain"))

    # Attach schedule.pdf file
    file_path = "schedule.pdf"
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(file_path)}",
        )
        message.attach(part)

    try:
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
        smtp.sendmail(
            SENDER_EMAIL_ADDRESS,
            receiver_email,
            message.as_string())
        print(f"Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email to {receiver_email}: {e}")
    finally:
        print("Closing the SMTP server connection...")
        # Close the SMTP server connection
        smtp.quit()
        print("SMTP server connection closed.")


# List of email addresses to send emails to
email_list = [
    "RECIPIENT_EMAIL_LIST",
]

# Send email to each address in the list
for email in email_list:
    send_email(email)
