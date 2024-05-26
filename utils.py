from config import *


def is_close() -> bool:
    """"Checks if latitude AND longitude of iss is within +/- 5 degree range of current position.
    Returns boolean."""

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    lat_check = MY_LAT-5 <= iss_latitude <= MY_LAT+5
    long_check = MY_LONG-5 <= iss_longitude <= MY_LONG+5
    combi_check = lat_check and long_check

    return combi_check


def is_dark() -> bool:
    """Checks if the current hour is after sunset or before sunrise.
    Returns boolean."""

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    current_hour = datetime.now().hour

    dark_check = current_hour <= sunrise_hour or current_hour >= sunset_hour

    return dark_check


def send_iss_notification_mail(receiver_email_address: str):
    """Sets up smtp email and sends to receiver email address."""
    email_message = (f"Subject: ISS overhead\n\nIf you look to the night sky right now, and the sky is clear,"
                     f"you should be able to see the International Space Station floating by.")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=GMAIL_ID, password=GMAIL_APP_PW)
        connection.sendmail(from_addr=GMAIL_ID, to_addrs=receiver_email_address,
                            msg=email_message)
