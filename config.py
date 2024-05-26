import requests
from datetime import datetime
import smtplib
from os import environ

MY_LAT = 52.162970
MY_LONG = 5.395200

GMAIL_ID = environ.get("GMAIL_ID")
GMAIL_APP_PW = environ.get("GMAIL_APP_PW")
