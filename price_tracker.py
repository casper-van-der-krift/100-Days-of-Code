import os
import smtplib
from dataclasses import dataclass
from src.utils import is_valid_email
from errors import InvalidEmailException
from src.config import *

"""
This class tracks the prices for products on the Amazon website.
It only works for the structure of the Amazon website.

"""


@dataclass
class AmazonPriceTracker:
    product_url: str
    target_price: float
    email_address: str

    def __post_init__(self):
        self._validate_email(self.email_address)

    @staticmethod
    def _validate_email(email):
        if not is_valid_email(email):
            raise InvalidEmailException("This is not a valid email address.")

    @property
    def _product_price(self):
        """
        Gets the product price from the product url.

        :return: price of the product as a float
        """
        # Get text from url using requests

        minimal_header = {
            "User-Agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "Accept-Language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7",
        }

        headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7",
                "Priority": "u=0, i",
                "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": r"\"Windows\"",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "cross-site",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            }

        response = requests.get(self.product_url, headers=headers)
        website = response.text

        # Create soup
        soup = BeautifulSoup(website, 'html.parser')
        print(f"Printed prettified soup:\n{soup.prettify()}")

        # Find tags with classes related to the price of the product
        price_symbol = soup.find(class_='a-price-symbol').text
        price_whole = soup.find(class_="a-price-whole").text
        price_fraction = soup.find(class_="a-price-fraction").text

        # Combine into single price
        price_float = float(price_whole + price_fraction)

        return price_float

    @property
    def _price_is_lower_than_target(self):
        return self._product_price < self.target_price

    def notify(self):
        if self._price_is_lower_than_target:
            self.send_notification_email()

    def send_notification_email(self):
        message = (f"Subject: Cheap Product Alert!\n\n"
                   f"Good day,\n\n"
                   f"The product of your interest is now cheaper than your target price.\n"
                   f"If you wish to purchase, you can find the product through this URL:\n{LIVE_URL}\n\n."
                   f"Kind regards,\n"
                   f"Casper")

        with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=os.environ["GMAIL_ID"], password=os.environ["GMAIL_APP_PW"])
            connection.sendmail(from_addr=os.environ["GMAIL_ID"], to_addrs=self.email_address, msg=message)
