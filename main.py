##################### Extra Hard Starting Project ######################

import datetime as dt
import smtplib
import pandas as pd
from random import randint


def write_email(name: str) -> str:
    """Chooses a random integer between 1-3 that corresponds to three templates of happy birthday letters.
    Takes a name as input that will replace the [NAME] placeholder in the templates.
    Returns the email contents with name as a string."""
    random_letter_file = f"letter_{randint(1, 3)}.txt"
    random_letter_path = f"./letter_templates/{random_letter_file}"

    with open(random_letter_path, mode='r') as file:
        contents = file.read()

    new_contents = contents.replace("[NAME]", name)

    return new_contents


# 1. Store .csv as dataframe
df = pd.read_csv('birthdays.csv')

# 2. Filter dataframe on birthdays matching today
now = dt.datetime.now()
today = now.day
this_month = now.month

current_month_day_filter = (df.month == this_month) & (df.day == today)
df_filtered = df[current_month_day_filter]

empty = df_filtered.empty

birthday_dict_list = df_filtered.to_dict(orient='records')


# 3. If there are matches - i.e. the dataframe is not empty - email to each person in the dataframe

if not empty:

    # Setup email parameters
    my_identity = "yung.biblebelt"
    my_password = "%$qgwJ*EJ89&gJ%"
    app_password = "nktimklcrbvmvoef"
    my_gmail_address = f"{my_identity}@gmail.com"

    # Get matching persons name and email and create a randomly chosen birthday email
    for person in birthday_dict_list:
        birthday_message = write_email(name=person['name'])
        email = person['email']

        email_message = f"Subject: Happy Birthday!\n\n{birthday_message}"

        # Use smtplib to create email connection and send messages
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_gmail_address, password=app_password)
            connection.sendmail(from_addr=my_gmail_address, to_addrs=email,
                                msg=email_message)















