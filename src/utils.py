from src.config import *


def input_date_format_validated() -> str:
    """Asks the user to put in a date through input prompt.
    Validates if the correct format YYYY-MM-DD is used.
    If not, a warning is printed and the function runs again.
    If correct, the date is returned as a string."""

    date = input("What year do you like to travel to? Type the day in this format: YYYY-MM-DD\n")

    try:
        if date != dt.datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d"):
            raise ValueError
        return date

    except ValueError:
        print("Invalid input. Type the day in this format: YYYY-MM-DD")
        return input_date_format_validated()


def clean_string(dirty_string: str) -> str:
    """Takes a string as input. First we search for the specific sequence of "\t\t\n\t\n\n\n\t\n\t";
     this sequence seperates artist from title. Separation sequence is replaced by '---'.
    The remaining \n and \t are stripped. Finally we filter for the values that contain 'NEW';
    which is noise slipping through our scraping process.
    Returns the cleaned string or None in case of noise (i.e. 'NEW')."""

    artist_title_separated = dirty_string.replace('\t\t\n\t\n\n\n\t\n\t', '---')
    cleaned_string = artist_title_separated.strip()
    if 'NEW' not in cleaned_string:
        return cleaned_string


def contains_letter(my_string: str) -> bool:
    """Takes a string as input and checks if it contains a letter.
    Returns True if so, otherwise returns False."""

    for c in my_string:
        if c.isalpha():
            return c.isalpha()

    return False
