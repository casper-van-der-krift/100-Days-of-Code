import os
from twilio.rest import Client
import smtplib


class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ.get('TWILIO_SID'), os.environ.get("TWILIO_AUTH_TOKEN"))
        self.gmail_id = os.environ.get("GMAIL_ID")
        self.gmail_pw = os.environ.get("GMAIL_APP_PW")

    def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.

        Parameters:
        message_body (str): The text content of the SMS message to be sent.

        Returns:
        None

        Notes:
        - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
        message = self.client.messages.create(
            from_=os.environ.get("TWILIO_VIRTUAL_NUMBER"),
            body=message_body,
            to=os.environ.get("TWILIO_VIRTUAL_NUMBER")
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)

    def send_email(self, message, email_address):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.gmail_id, password=self.gmail_pw)
            connection.sendmail(from_addr=self.gmail_id, to_addrs=email_address,
                                msg=message)
