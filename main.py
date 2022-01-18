from tkinter import *
import pandas as pd
import locale
import random

BACKGROUND_COLOR = "#B1DDC6"
random_word = {}

# __________________________________READING CSV__________________________________#
locale.setlocale(locale.LC_ALL, "Turkish")
try:
    file = pd.read_csv('./data/Words_to_learn.csv')
except FileNotFoundError:
    file = pd.read_csv('./data/Turkish Words.csv')
dictionary = file.to_dict(orient='records')




# ___________________________________FUNCTIONS___________________________________#
def exit_dict():
    window.destroy()


def correct():
    next_card()
    dictionary.remove(random_word)
    new_data = pd.DataFrame.from_dict(dictionary)
    new_data.to_csv('./data/Words_to_learn.csv', index=False)


def next_card():
    global timer, random_word
    window.after_cancel(timer)
    random_word = random.choice(dictionary)
    canvas.itemconfig(image, image=front_card)
    canvas.itemconfig(card_title, fill='black', text='Turkish')
    canvas.itemconfig(card_word, fill='black', text=random_word['Turkish'])
    window.after(5000, flip_card)


def flip_card():
    global random_word
    canvas.itemconfig(image, image=back_card)
    canvas.itemconfig(card_title, fill='white', text='English')
    canvas.itemconfig(card_word, fill='white', text=random_word['English'])


# _____________________________________LAYOUT_____________________________________#

# window
window = Tk()
window.title('Turkish Learn Game')
window.config(padx=50, pady=50, width=1000, height=800, bg=BACKGROUND_COLOR)
timer = window.after(5000, next_card)

# photos
front_card = PhotoImage(file='./images/card_front.png')
back_card = PhotoImage(file='./images/card_back.png')
right = PhotoImage(file='./images/right.png')
wrong = PhotoImage(file='./images/wrong.png')
Exit = PhotoImage(file='./images/exit.png')

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(400, 264, image=front_card)
card_title = canvas.create_text(400, 150, text='title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))
canvas.grid(columnspan=3)

# right, wrong:
right_logo = Button(width=100, height=100, image=right, bg=BACKGROUND_COLOR, highlightthickness=0, command=correct)
right_logo.grid(column=2, row=1)

# wrong button:
wrong_logo = Button(width=100, height=100, bg=BACKGROUND_COLOR, image=wrong, highlightthickness=0, command=next_card)
wrong_logo.grid(column=0, row=1)

# Exit button:
exit_logo = Button(image=Exit, text='Exit ', bg=BACKGROUND_COLOR, fg='black', command=exit_dict, font=('Arial', 20, ''))
exit_logo.grid(column=1, row=2)

next_card()
window.mainloop()
