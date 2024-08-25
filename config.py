import requests
from bs4 import BeautifulSoup
import re
import smtplib
from os import environ
import os
from dotenv import load_dotenv

load_dotenv()

STATIC_SITE_URL = "https://appbrewery.github.io/instant_pot/"
LIVE_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
