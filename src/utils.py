from src.config import *


def write_email(name: str) -> str:
    """Chooses a random integer between 1-3 that corresponds to three templates of happy birthday letters.
    Takes a name as input that will replace the [NAME] placeholder in the templates.
    Returns the email contents with name as a string."""
    random_letter_file = f"letter_{randint(1, 3)}.txt"

    # Als je folder paths doet zou ik altijd "join" gebruiken van de ingebouwde library "os", 
    # dan weet je zeker dat je script werkt op Windows, MacOS en Linux. 
    # Bij al die systemen zijn de slashes enzo allemaal net anders en soms werkt het dan niet.
    random_letter_path = join(
        TEMPLATES_FOLDER,
        random_letter_file
    )
    with open(random_letter_path, mode='r') as file:
        contents = file.read()

    new_contents = contents.replace("[NAME]", name)

    return new_contents


def send_emails(df: pd.DataFrame):
    # Get matching persons name and email and create a randomly chosen birthday email

    # df.iterrows() laat je over de rijen van een dataframe loopen. 
    # Dit is niet aan te raden voor grote dataframes, want daar zijn weer andere opties voor zoals bijvoorbeeld:
    # df.apply(lambda row: send_email(row), axis=1)  <- dit loopt ook over iedere rij en per rij runt het de functie 'send_email()'
    # Bovenstaande is ter kennisgeving ;) 

    for i, row in df.iterrows():
        # In dit geval (met iterrows) krijg je een tuple met de index en de row in de dataframe vandaar i, row.
        # Die 'row' kun je op een zelfde manier gebruiken als jou 'person' variable. 
        # Je mag deze van mij ook gewoon person noemen hoor (dus i, person)
        birthday_message = write_email(name=row['name'])
        receiver = row['email']

        email_message = f"Subject: Happy Birthday!\n\n{birthday_message}"

        # Use smtplib to create email connection and send messages
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=GMAIL_ADDRESS, password=APP_PW)
            connection.sendmail(from_addr=GMAIL_ADDRESS, to_addrs=receiver,
                                msg=email_message)