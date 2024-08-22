import datetime as dt
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
import pprint
from os import environ

BASE_URL = "https://www.billboard.com/charts/hot-100"
SPOTIFY_CLIENT_ID = environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = environ.get("SPOTIFY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = "https://example.com/"
