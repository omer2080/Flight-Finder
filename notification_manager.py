import getpass
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
        MESSAGE = f"""Subject: Cheap Flight Alert
Hi There,

I found the perfect flight for you!

Price: {self.price}$
Location: {self.destination_city}-{self.destination_airport}
Dates: {self.depart_date} to {self.return_date}

Enjoy!
"""
    
        smtp = smtplib.SMTP(HOST, PORT)
        status_code, response = smtp.ehlo()
        # print(f"[*] Echoing the server: {status_code}{response}")
        status_code, response = smtp.starttls()
        # print(f"[*] Starting TLS connection: {status_code}{response}")
        status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
        # print(f"[*] Logging in: {status_code}{response}")


        smtp.sendmail(FROM_EMAIL, TO_EMAIL_1, MESSAGE)
        smtp.sendmail(FROM_EMAIL, TO_EMAIL_2, MESSAGE)
        
        smtp.quit()

            
        
        
        
        
        









