from email.mime.multipart import MIMEMultipart
import random
import smtplib
from email.mime.text import MIMEText
from flight_data import FlightData

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "omer2080101@outlook.co.il"
TO_EMAIL_1 = "omer208010@gmail.com"
TO_EMAIL_2 = "romy.attar@gmail.com"

KIWI_STARTING_LINK = "https://www.kiwi.com/en/booking?booking_token="

list_of_sentences = ["Your Unbeatable Deal Awaits!",
                    "Found Your Next Vacation!",
                    "Unforgettable Adventure Awaits!",
                    "Uncovered Your Ideal Vacation!",
                    "Your ideal Getaway Located!",
                    "Unbeatable deals on your radar!"
                    ]

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, data:FlightData):
        self.price = data.price
        self.origin_city = "Tel Aviv"
        self.destination_city = data.destination_city
        self.destination_airport = data.destination_airport
        self.depart_date = data.depart_date
        self.return_date = data.return_date
        self.flight_link = data.flight_link
        
        
    def mail_sender(self, PASSWORD):
        # Read HTML content from file
        with open("mail.html", "r") as file:
            html_content = file.read()

        # Substitute actual values into the placeholders
        formatted_message = html_content.format(
            price = self.price,
            destination_city = self.destination_city,
            destination_airport = self.destination_airport,
            depart_date = self.depart_date,
            return_date = self.return_date,
            random_phrase = random.choice(list_of_sentences),
            flight_link = KIWI_STARTING_LINK + self.flight_link

        )
        
        # Create a MIMEMultipart message
        message = MIMEMultipart("alternative")
        message['Subject'] = "YOUR NEXT FLIGHT HAS BEEN FOUND"

        # Attach HTML-formatted content to the email message
        html_part = MIMEText(formatted_message, 'html')
        message.attach(html_part)

        #connecting to the Outlook SMTP server
        smtp = smtplib.SMTP(HOST, PORT)
        
        #upgrade the connection to a secure TLS (Transport Layer Security) or SSL (Secure Sockets Layer) connection.
        smtp.starttls()
        
        #authenticate the user
        smtp.login(FROM_EMAIL, PASSWORD)

        smtp.sendmail(FROM_EMAIL, TO_EMAIL_1, message.as_string())
        # smtp.sendmail(FROM_EMAIL, TO_EMAIL_2, message.as_string())
        
        smtp.quit()

            
        
        
        
        
        









