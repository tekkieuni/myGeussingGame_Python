import pygame
from TekkiePygameLib import Button, InputBox, Label


WIN_WIDTH = 500
WIN_HEIGHT = 500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (192, 192, 192)
MY_COLOR_1 = (184, 220, 210)
MY_COLOR_2 = (8, 55, 81)

guessing_game_win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Guessing Game")


header = Label(x=250, y=39, text="Guessing Game", color=MY_COLOR_2, size=40)
min_label = Label(x=70, y=91, text="Min Value:", color=BLACK, size=20)
max_label = Label(x=70, y=122, text="Max Value:", color=BLACK, size=20)
guess_title = Label(x=250, y=277, text="Guess No. 1", color=BLACK, size=18)
feedback = Label(x=250, y=435, text="Guess The number!", color=BLUE, size=20)
message = Label(x=250, y=170, text="", color=GREEN, size=20)
name_label = Label(x=350, y=100, text="Your Name", color=BLACK, size=20)
welcome_message = Label(x=350, y=80, text="Please enter your name", color=BLUE, size=20)

#  list of all labels
all_labels = [header, min_label, max_label, guess_title, feedback, message, name_label, welcome_message]

user_min = InputBox(x=160, y=92)
user_max = InputBox(x=160, y=123)
user_guess = InputBox(x=250, y=311)
user_name = InputBox(x=350, y=123)

#  list of all text entry field
all_text_entry_field = [user_min, user_max, user_guess, user_name]

generate_random_button = Button(x=250, y=200, width=101, height=22, text='Generate Number', color=GRAY,
                                outline_color=BLUE)
guess_button = Button(x=250, y=340, width=50, height=22, text='Guess!', color=BLUE, outline_color=GRAY)
reset_button = Button(x=450, y=450, width=45, height=22, text='Reset', color=GRAY, outline_color=GREEN)

#  list of all buttons
all_buttons = [generate_random_button, guess_button, reset_button]


