from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass
import random
from flight_data import FlightData
import smtplib
from dotenv import load_dotenv

load_dotenv()

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "omer2080101@outlook.co.il"
PASSWORD = getpass.getpass("Enter The Mail Password: ")
TO_EMAIL_1 = "omer208010@gmail.com"
TO_EMAIL_2 = "romy.attar@gmail.com"

set_of_sentences = ["Your Unbeatable Deal Awaits!",
                    "Found Your Next Vacation!",
                    "Unforgettable Adventure Awaits!",
                    "Uncovered Your Ideal Vacation!",
                    "Your ideal Getaway Located!",
                    "Unbeatable deals on your radar!"
                    ]


message = MIMEMultipart("alternative")
message['Subject'] = "YOUR NEXT FLIGHT HAS BEEN FOUND"
message['From'] = FROM_EMAIL
message['To'] = TO_EMAIL_1
message['Cc'] = FROM_EMAIL
message['Bcc'] = FROM_EMAIL

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, data:FlightData):
        self.price = data.price
        self.origin_city = "Tel Aviv"
        self.destination_city = data.destination_city
        self.destination_airport = data.destination_airport
        self.depart_date = data.depart_date
        self.return_date = data.return_date
        
    def mail_sender(self):
        # Read HTML content from file
        with open("mail.html", "r") as file:
            html_content = file.read()

        # Substitute actual values into the placeholders
        formatted_message = html_content.format(
            price=self.price,
            destination_city=self.destination_city,
            destination_airport=self.destination_airport,
            depart_date=self.depart_date,
            return_date=self.return_date,
            random_phrase = random.choice(set_of_sentences)

        )
                
        html_part = MIMEText(formatted_message, 'html')
        message.attach(html_part)
    
        smtp = smtplib.SMTP(HOST, PORT)
        status_code, response = smtp.ehlo()
        #print(f"[*] Echoing the server: {status_code}{response}")
        status_code, response = smtp.starttls()
        #print(f"[*] Starting TLS connection: {status_code}{response}")
        status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
        #print(f"[*] Logging in: {status_code}{response}")


        smtp.sendmail(FROM_EMAIL, TO_EMAIL_1, message.as_string())
        smtp.sendmail(FROM_EMAIL, TO_EMAIL_2, message.as_string())
        
        smtp.quit()

            
        
        
        
        
        









