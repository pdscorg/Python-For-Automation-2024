# Day 3 | Email Automation

## Setting Up

1. Cloning the repository

   ```bash
   git clone git@github.com:pdscorg/Python-For-Automation-2024.git
   cd Day_03/
   ```

2. Create a `virtual environment`

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Head over to this [video](https://www.youtube.com/watch?v=27NianZC7Wk) and generate `APP_PASSWORD`.

## Sending Basic Mail

1. Change your directory to `01_basic_email/start`

   ```bash
   cd 01_basic_email/start
   ```

2. Replace the `None` with the respective value

   ```python
   # Define your SMTP server details
   SMTP_SERVER = "smtp.gmail.com"
   SMTP_SERVER_PORT = 587

   # Define your sender email address and password
   SENDER_EMAIL_ADDRESS = "YOUR_EMAIL_ADDRESS"
   SENDER_EMAIL_PASSWORD = "YOUR_APP_PASSWORD"

   # Define the receiver email address
   RECEIVER_EMAIL_ADDRESS = "RECEIVER_EMAIL_ADDRESS"

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
   ```

3. Now, run the `send_mail.py` script to send the mail

   ```bash
   python send_mail.py
   ```

4. Change your directory back to normal

   ```bash
   cd ../../
   ```

5. If you encounter any error, you can checkout the [final code](/01_basic_email/end/send_mail.py).

## Email with `.env`

With the above implementation, the code directly includes **sensitive information**(**such as email credentials**) within the script, which can lead to **security risks** _if the script is shared or stored insecurely_.

The solution to above problem is to stored those value in the .env file

1. Change your directory to `02_env_file/start`

   ```bash
   cd 02_env_file/start
   ```

2. Rename `.env.example` to `.env`file and update it.

   ```env
   SMTP_SERVER=smtp.gmail.com
   SMTP_SERVER_PORT=587
   SENDER_EMAIL_ADDRESS=YOUR_EMAIL_ADDRESS
   SENDER_EMAIL_PASSWORD=YOUR_EMAIL_PASSWORD
   RECEIVER_EMAIL_ADDRESS=RECEIVER_EMAIL_ADDRESS
   ```

3. Update the code

   - Load the **environment variables**

     ```python
     from dotenv import load_dotenv
     import os

     load_dotenv()
     ```

   - Using the **environment variables**

     ```python
     SMTP_SERVER = os.getenv("SMTP_SERVER")
     SMTP_SERVER_PORT = os.getenv("SMTP_SERVER_PORT")
     SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")
     SENDER_EMAIL_PASSWORD = os.getenv("SENDER_EMAIL_PASSWORD")
     RECEIVER_EMAIL_ADDRESS = os.getenv("RECEIVER_EMAIL_ADDRESS")
     ```

     ```python
     smtp = smtplib.SMTP(SMTP_SERVER, int(SMTP_SERVER_PORT))
     ```

4. Now, run the python script to send the email

   ```bash
   python email_with_env.py
   ```

5. Change your directory back to normal

   ```bash
   cd ../../
   ```

6. If you encounter any error, you can checkout the [final code](/02_env_file/end/email_with_env.py)

## Email with attachment

Upto now, we have send plain text mail. The limitation of plain text mail are as follows:

- No support for rich text(HTML)
- Cannot include attachments or multimedia
- Limited to simple text messages

The solution is to use **Multipurpose Internet Mail Extensions(MIME)**.

**MIME**

- allows for multiple parts in an email(_plain text, HTML, attachments_).
- supports different content types(_text, images, files_).
- essential for professional and feature-rich emails.

1. Change your directory to `cd 03_single_attachment/start`

   ```bash
   cd 03_single_attachment/start
   ```

2. Update your `subject` and `body` of the mail

   ```python
   subject = "PDSC Python for Automation Workshop - Certificate of Participation"
   ```

   ```python
   body = """Dear Participant,
   Thank you for participating in the PDSC Python for Automation workshop!
   Attached to this email, you will find your certificate of participation.
   We hope you found the workshop informative and valuable. Should you have any questions or feedback, feel free to reach out to us.
   Best regards,
   PDSC Team
   """
   ```

3. Using **MIME** to add attachments

   - Importing necessary modules

     ```python
     from email.mime.multipart import MIMEMultipart
     from email.mime.text import MIMEText
     from email.mime.base import MIMEBase
     from email import encoders
     ```

   - Creating **MIME Object**

     ```python
      message = MIMEMultipart()
      message["Subject"] = subject
      message["From"] = SENDER_EMAIL_ADDRESS
      message["To"] = RECEIVER_EMAIL_ADDRESS
      message.attach(MIMEText(body, "plain"))
     ```

   - Adding the attachment

     ```python
      file_path = "schedule.pdf"
      attachment = open(file_path, "rb")
      part = MIMEBase("application", "octet-stream")
      part.set_payload(attachment.read())
      encoders.encode_base64(part)
      part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(file_path)}"
      )
      message.attach(part)
     ```

   - Updating the parameter of `smtp.sendmail()`

     ```python
     smtp.sendmail(SENDER_EMAIL_ADDRESS, RECEIVER_EMAIL_ADDRESS, message.as_string())
     ```

4. Copy the `.env` file you have created before into `03_single_attachment/start` folder

5. Now, run the python script to send the email

   ```bash
   python single_attachment_mail.py
   ```

6. Change your directory back to normal

   ```bash
   cd ../../
   ```

7. If you encounter any error, you can checkout the [final code](/03_single_attachment/end/single_attachment_mail.py)

## HTML Email

1. Change your directory to `cd cd 04_html_content/start`

   ```bash
   cd cd 04_html_content/start
   ```

2. Copy `../end/email.html`

   ```bash
   cp ../end/email.html email.html
   ```

3. Update the [`html_email.py`](./04_html_content/start/html_email.py)

   - Import `MIMEImage` and update `subject` and `body`

     ```python
     from email.mime.image import MIMEImage
     ```

     ```python
     subject = "Congratulations on Completing the Workshop!"
     ```

     ```python
     plain_text_body = """
     Dear Participant,

     Congratulations on successfully completing the PDSC: Python for Automation workshop!

     We are pleased to present you with a certificate of participation, which is attached to this email.

     We hope you found the workshop informative and engaging. Thank you for your participation.

     Best regards,
     Susheel Thapa
     """
     ```

   - Adding [`email.html`](./04_html_content/start/email.html) and [logo](./04_html_content/start/pdsc_logo.png) as an attachment to email.

     ```python
     with open("email.html", "r") as file:
        html_body = file.read()
     ```

     ```python
     message = MIMEMultipart("alternative")
     ```

     ```python
     part1 = MIMEText(plain_text_body, "plain")
     message.attach(part1)
     ```

     ```python
     part2 = MIMEText(html_body, "html")
     message.attach(part2)
     ```

     ```python
     with open("pdsc_logo.png", "rb") as image_file:
        image = MIMEImage(image_file.read())
        image.add_header('Content-ID', '<pdsc_logo>')
        message.attach(image)
     ```

4. Copy the `.env` file you have created before and `schedule.pdf` into `04_html_content/start` folder

5. Now, run the python script to send the email

   ```bash
   python html_email.py
   ```

6. Change your directory back to normal

   ```bash
   cd ../../
   ```

7. If you encounter any error, you can checkout the [final code](/04_html_content/end/html_email.py)

## Sending Multiple Email

### Function in Python

A fuction is a block of code that performs a spefific task.

```python
def send_email(receiver_email):
   # Logic to send the single email
   pass
```

### `for` loop in Python

In Python ,we use for loop to iterate over various sequences such as **lists**, **tuples**, **sets**, **strings** or **dictionaries**.

```python
for email in email_list:
   send_mail(email)
```

1. Change your directory to `cd 05_multiple_emails/start`

   ```bash
   cd 05_multiple_emails/start
   ```

2. Let's encapsulate the logic to send singel mail in a function name `send_mail()`

   ```python
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
   ```

3. Iterate the email list and call `send_mail()` function.

   ```python
   email_list =["RECIPIENT_EMAIL_LIST"]

   for email in email_list:
      send_email(email)
   ```

   _Note: Write valid email inplace of `RECIPIENT_EMAIL_LIST`_

4. Copy the `.env` file you have created before and `schedule.pdf` into `05_multiple_emails/start` folder

5. Now, run the python script to send the email

   ```bash
   python sending_multiple_email.py
   ```

6. Change your directory back to normal

   ```bash
   cd ../../
   ```

7. If you encounter any error, you can checkout the [final code](./05_multiple_emails/end/sending_multiple_email.py)

## Dynamic Mail via CSV

1. Change your directory to `cd 06_dynamic_emails/start`

   ```bash
   cd 06_dynamic_emails/start
   ```

2. Create a sample csv file (`sample.csv`)

   ```csv
   Name,Email
   name_of_person, email_address_of_person
   ```

3. Loading `sample.csv` via `pandas`

   ```python
   import pandas as pd

   df = pd.read_csv("./sample.csv")

   for index, row in df.iterrows():
      print(row["Name"], row["Email"])
   ```

4. Updating [`dynamic_mail.py`](./06_dynamic_emails/start/dynamic_mail.py)

   ```python
   import pandas as pd

   df = pd.read_csv("./sample.csv")

   for index, row in df.iterrows():
      name = row["Name"]
      email = row["Email"]
      print(name, email)
      send_email(email, name)
   ```

5. Copy the `.env` file you have created before and `schedule.pdf` into `06_dynamic_emails/start` folder

6. Now, run the python script to send the email

   ```bash
   python dynamic_mail.py
   ```

7. Change your directory back to normal

   ```bash
   cd ../../
   ```

8. If you encounter any error, you can checkout the [final code](./06_dynamic_emails/end/dynamic_mail.py)
