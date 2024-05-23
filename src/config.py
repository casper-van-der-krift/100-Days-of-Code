##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
from random import randint
import pandas as pd

from os.path import join
from os import environ

# Je templates folder is een constant, die zou ik gewoon boven aan je script zetten
TEMPLATES_FOLDER = 'letter_templates'
DATA_FOLDER = 'data'  # zelfde geld voor je Data Folder (die ik nu ff gemaakt hebt)
BIRTHDAY_FILE = 'birthdays.csv'  # en je birthday file


"""Je credentials kun je het beste lokaal op je eigen PC opslaan. 
Op Windows doe je dit door nieuwe Environment Variables toe te voegen. 
Op Windows moet je daarna wel je PC ff opnieuw opstarten, anders pakt hij ze niet.
Je kunt dit doen via Control Panel (of ff Environment Variables zoeken in je Start menu) en
Je kunt dit volgens mij ook doen met `SETX GMAIL_ID="yung.biblebelt"`
Die environment variables kun je vervolgens inladen met os.environ.get()
Hiermee voorkom je dat je perongeluk wachtwoorden bijvoorbeeld op Github hebt staan"""
GMAIL_ID = environ.get("GMAIL_ID")
GMAIL_PW = environ.get("GMAIL_PW")
APP_PW = environ.get("APP_PW")

GMAIL_ADDRESS = f"{GMAIL_ID}@gmail.com"

