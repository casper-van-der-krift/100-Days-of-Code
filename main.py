from utils import is_close, is_dark, send_iss_notification_mail
import time

if __name__ == "__main__":

    while True:
        time.sleep(60)
        if is_dark() and is_close():
            send_iss_notification_mail(receiver_email_address="caspervanderkrift@gmail.com")

