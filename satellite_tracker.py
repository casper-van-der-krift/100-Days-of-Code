from dataclasses import dataclass 

from utils import get_request, is_valid_email
from errors import MissingISSPositionError, MissingSunDataError, InvalidEmailException

"""
Ik weet niet of je al eens van 'decorators' gehoord hebt, maar die zie je hieronder
Die kun je toevoegen aan functies en classes om speciale functionaliteiten mee te geven

In dit geval geven we de Satellite class mee dat het een 'dataclass' is.
Dit houdt in dat deze class zich iets anders gedraagd dan een normale class.

Een van de voordelen van deze specifieke decorator is dat je nu niet allemaal code hoeft te typen zoals

class Satellite:
    def __init__(self, var_a, var_b, var_c):
        self.var_a = var_a
        self.var_b = var_b 
        self.var_c = var_c

Dit stuk wordt opgevangen door de decorator, dus kun je gewoon doen zoals hieronder
"""

ISS_API_URL = "http://api.open-notify.org/iss-now.json"
SUNSET_API_URL = "https://api.sunrise-sunset.org/json"

@dataclass
class SatelliteTracker:
    lat: float
    lon: float
    email: str

    """
    Deze __post_init__ functie is typisch iets van dataclasses, 
    deze functie word meteen geroepen na initialisatie van de class
    Hier kun je dus bijvoorbeeld checks uitvoeren over je input (is emailadres valid in dit geval)
    Maar ook andere dingen doen die je mogelijk nog hebt meteen na initialisatie 
    """
    def __post_init__(self):
        self._validate_email(self.email)

    @staticmethod
    def _validate_email(email):
        """
        Een 'staticmethod' is een functie in een class die geen 'self' gebruikt
        """
        if not is_valid_email(email):
            raise InvalidEmailException("Gappie dit is geen email adres")

    @property  
    def _is_close(self):
        """
        De property decorator maakt dat je SatelliteTracker.is_close kan doen, 
        zonder dat het een 'function-call' is. Dus geen haakjes en je
        kunt ook geen parameters meesturen, maar dat is voor deze functie toch niet nodig
        """

        data = get_request(url=ISS_API_URL)

        """
        Als de key "iss_position" niet bestaat, is de waarde None
        Dit werkt een beetje zoals:
        try:
            iss_position = data["iss_position"]
        except KeyError:
            iss_position = None
        We doen dit voor het geval er ineens geen iss_position mee komt en er dus iets fout gaat
        """

        iss_position = data.get("iss_position", None)  
        if iss_position:
            # Eigenlijk zou je het zelfde hier nog een keer willen doen voor als mogelijk "latitude" en/of "longitude" ineens niet bestaan
            iss_latitude = float(iss_position["latitude"])
            iss_longitude = float(iss_position["longitude"])

            """
            Je zou hieronder de +/-5 nog kunnen aanpassen, en mogelijk als parameter in 
            is_close kunnen meegeven. Dan moet je wel de property decorater weghalen en weer SatelliteTracker.is_close() callen
            """

            lat_check = self.lat - 5 <= iss_latitude <= self.lat + 5
            long_check = self.lon - 5 <= iss_longitude <= self.lon + 5
            combi_check = lat_check and long_check

            return combi_check
        else:
            raise MissingISSPositionError("Missing ISS Postion...")

    @property
    def _is_dark(self) -> bool:
        """
        Methods starting with '_' are private and can't be called outside the scope of the class
        We do this when calling the method doesn't make any sense without the context of the class
        """

        parameters = {
            "lat": self.lat,
            "lng": self.lon,
            "formatted": 0,
        }

        data = get_request(url=SUNSET_API_URL, parameters=parameters)

        sun_results = data.get("results", None)
        if sun_results:

            sunrise_hour = int(sun_results["sunrise"].split("T")[1].split(":")[0])
            sunset_hour = int(sun_results["sunset"].split("T")[1].split(":")[0])

            current_hour = datetime.now().hour

            dark_check = current_hour <= sunrise_hour or current_hour >= sunset_hour

            return dark_check
        else:
            raise MissingSunDataError("Kut de zon is stuk!")

    def notify(self):
        if self._is_close and self._is_dark:
            self.send_notification()
    
    def send_notification(self):
        """Sets up smtp email and sends to receiver email address."""

        email_message = (f"Subject: ISS overhead\n\nIf you look to the night sky right now, and the sky is clear,"
                        f"you should be able to see the International Space Station floating by.")
        
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(
                user=GMAIL_ID, 
                password=GMAIL_APP_PW
            )
            connection.sendmail(
                from_addr=GMAIL_ID, 
                to_addrs=self.email,
                msg=email_message
            )