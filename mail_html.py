    import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP server details
HOST = "smtp-mail.outlook.com"
PORT = 587

# Email details
FROM_EMAIL = "<add from email address here>"
TO_EMAIL = "<add to email address here>"
PASSWORD = getpass.getpass("Enter password: ")  # Use getpass to securely input the password

# Create an email message
message = MIMEMultipart("alternative")
message['Subject'] = "<add subject here>"
message['From'] = FROM_EMAIL
message['To'] = TO_EMAIL
message['Cc'] = FROM_EMAIL
message['Bcc'] = FROM_EMAIL

# Read the HTML content from a file
html = ""
with open("mail.html", "r") as file:
    html = file.read()

# Attach HTML content to the email message
html_part = MIMEText(html, 'html')
message.attach(html_part)

# Connect to the SMTP server
smtp = smtplib.SMTP(HOST, PORT)

# Start a connection and upgrade it to a secure TLS connection
status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")

# Login to the SMTP server using the provided email and password
status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in: {status_code} {response}")

# Send the email
smtp.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())

# Quit the SMTP session
smtp.quit()
