from tkinter import *
import pandas as pd
from random import choice

# THIS IS A LEARNING PROGRAM TO LEARN THE CAPITALS OF THE WORLD
# IT WORKS AS A PILE OF CARDS THAT SHOW THE COUNTRY NANE ON THE FRONT SIDE OF THE CARD AND THE CAPITAL ON THE BACK
# AFTER 3 SECONDS, THE CARD FLIPS FROM FRONT TO BACK
# USER NOW HAS THE CHOICE TO PRESS TWO BUTTONS:
#   -THE CORRECT BUTTON IF YOU KNEW THE ANSWER: CARD IS NOW REMOVED FROM THE PILE OF CARDS, I.E. IT WON'T SHOW UP AGAIN
#   -THE WRONG BUTTON IS PRESSED WHEN USER DID NOT KNOW THE ANSWER, I.E. CARD GOES BACK IN THE PILE
# WHEN USER CLOSES THE PROGRAM, THE PROGRESS IS SAVED. I.E. THE SAME PILE OF CARDS IS LOADED WHEN RESTARTING


# FUNCTIONS

def next_card_correct():
    """Is called when the 'correct' button is pressed:
        -Resets the timer
        -Removes the card from the pile, i.e. removes card from the database"""

    global current_word, flip_timer, all_capitals

    # Cancel timer
    window.after_cancel(flip_timer)

    # Remove current card
    all_capitals.remove(current_word)
    df_updated = pd.DataFrame.from_records(all_capitals)
    df_updated.to_csv("./data/words_to_learn.csv", index=False)

    # If pile is not empty yet
    if len(all_capitals) > 0:

        # Choose new country and format the interface
        current_word = choice(all_capitals)

        canvas.itemconfig(word_text, text=current_word['country'], fill="black")
        canvas.itemconfig(title_text, text="Country", fill="black")
        canvas.itemconfig(canvas_image, image=card_front_img)

        # Restart timer
        flip_timer = window.after(3000, flip_card)

    # If pile is empty: congratulate user and disable buttons
    else:
        canvas.itemconfig(word_text, text="All words learned!", fill="black")
        canvas.itemconfig(title_text, text="Congrats!", fill="black")
        button_correct.config(state='disabled')
        button_wrong.config(state='disabled')


def next_card_wrong():
    """Is called when the 'wrong' button is pressed. Does NOT remove a card and picks another one."""

    global current_word, flip_timer

    # Cancel timer
    window.after_cancel(flip_timer)

    # Choose new country
    current_word = choice(all_capitals)

    # Format interface with new country
    canvas.itemconfig(word_text, text=current_word['country'], fill="black")
    canvas.itemconfig(title_text, text="Country", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)

    # Restart timer
    flip_timer = window.after(3000, flip_card)


def flip_card():
    """Flips the card from country to capital. Searches the corresponding capital and reformat card. """
    global current_word

    # Tap in to the current capital-country dictionary and choose the captial. Reformat card.
    canvas.itemconfig(word_text, text=current_word['capital'], fill="white")
    canvas.itemconfig(title_text, text="Capital", fill='white')
    canvas.itemconfig(canvas_image, image=card_back_img)


# CONSTANTS

BACKGROUND_COLOR = "#B1DDC6"
IMAGE_WIDTH = 800
IMAGE_HEIGHT = 526
FONT_NAME = "Arial"
current_word = {}


# STEP 1: BUILD UI WITH TKINTER

# Create screen
window = Tk()
window.title("Capitals of the World")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Delay flipping card and store in variable to access in functions
flip_timer = window.after(3000, flip_card)

# Use Canvas to create the background image
canvas = Canvas(width=IMAGE_WIDTH, height=IMAGE_HEIGHT)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(IMAGE_WIDTH/2, IMAGE_HEIGHT/2, image=card_front_img)

# Use Canvas to create the text on the card
title_text = canvas.create_text(IMAGE_WIDTH/2, IMAGE_HEIGHT/2 - 120, text='Country', fill='black', font=(FONT_NAME, 35, 'italic'))
word_text = canvas.create_text(IMAGE_WIDTH/2, IMAGE_HEIGHT/2 + 20, text='Far away', fill='black', font=(FONT_NAME, 50, 'bold'))
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Create correct button
button_correct_img = PhotoImage(file="./images/right.png")
button_correct = Button(image=button_correct_img, highlightthickness=0, command=next_card_correct)
button_correct.grid(column=0, row=1)

# Create wrong button
button_wrong_img = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=button_wrong_img, highlightthickness=0, command=next_card_wrong)
button_wrong.grid(column=1, row=1)


# STEP 2: read .csv-data of Country/Capitals

# Read .csv-data with pandas

try:
    df = pd.read_csv("./data/words_to_learn.csv")
    if df.empty:
        df = pd.read_csv("./data/capitals.csv")

except FileNotFoundError:
    df = pd.read_csv("./data/capitals.csv")

finally:
    all_capitals = df.to_dict(orient='records')

# Run function once to get rid of placeholder texts in canvas
next_card_wrong()

window.mainloop()

