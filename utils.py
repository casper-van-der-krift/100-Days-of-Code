from config import *


def get_request(url, parameters=None):
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    data = response.json()
    return data


def is_valid_email(email):
    "FF ChatGPT een regex laten maken om emails te validaten"
    # Define the regex for validating an email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the regex
    if re.match(email_regex, email):
        return True
    else:
        return False
