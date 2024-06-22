import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Define your SMTP server details from environment variables
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_SERVER_PORT = os.getenv("SMTP_SERVER_PORT")

# Define your sender email address and password from environment variables
SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")
SENDER_EMAIL_PASSWORD = os.getenv("SENDER_EMAIL_PASSWORD")

# Define the subject for the email
subject = "PDSC Python for Automation Workshop - Day 3 Assignment | Auto send emails by attaching image as PDF attachment"

def load_html_template(file_path):
    """Load HTML template file and return its content."""
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    return html_content

def send_email(receiver_email, receiver_name, html_content):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = SENDER_EMAIL_ADDRESS
    message["To"] = receiver_email

    # Replace placeholder with recipient's name
    personalized_html_content = html_content.replace("Dear Participant,", f"Dear {receiver_name},")

    # Attach HTML content
    message.attach(MIMEText(personalized_html_content, "html"))

    # Attach assignment.py file
    file_path = "./assignment.py"
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {os.path.basename(file_path)}",
        )
        message.attach(part)

    with open("pdsc_logo.png", "rb") as image_file:
        image = MIMEImage(image_file.read())
        image.add_header('Content-ID', '<pdsc_logo>')
        message.attach(image)
    try:
        print(f"Initializing SMTP server connection for {receiver_email}...")
        # Initialize the SMTP server connection
        smtp = smtplib.SMTP(SMTP_SERVER, int(SMTP_SERVER_PORT))

        print(f"Starting TLS encryption for {receiver_email}...")
        # Start TLS encryption
        smtp.starttls()

        print(f"Logging in to the SMTP server for {receiver_email}...")
        # Login to the SMTP server
        smtp.login(SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD)

        print(f"Sending the email to {receiver_email}...")
        # Send the email
        smtp.sendmail(
            SENDER_EMAIL_ADDRESS,
            receiver_email,
            message.as_string())
        print(f"Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email to {receiver_email}: {e}")
    finally:
        print(f"Closing the SMTP server connection for {receiver_email}...")
        # Close the SMTP server connection
        smtp.quit()

# Load HTML template
html_content = load_html_template("assignment.html")

# Read the CSV file
df = pd.read_csv("./sample.csv")

# Send email to each address in the list
for index, row in df.iterrows():
    receiver_name = row["Name"]
    receiver_email = row["Email"]
    send_email(receiver_email, receiver_name, html_content)
