from myGuessingGameGUI import *
from myGuessingGame import *
import asyncio
#
# random_number = None
# counting_guesses = 1
# mouse_up = False


async def run():
    random_number = None
    counting_guesses = 1
    mouse_up = False

    while True:
        guessing_game_win.fill(MY_COLOR_1)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            for text_entry_field in all_text_entry_field:
                text_entry_field.handle_event(event)

        if generate_random_button.is_clicked():
            if random_number is None:
                random_number = input_range(int(user_min.text), int(user_max.text), message)
                print(random_number)

        if guess_button.is_clicked():
            if not mouse_up:
                if random_number is None:
                    message.set_text("First - generate number!")
                else:
                    if not time_to_guess(random_number, int(user_min.text), int(user_max.text),
                                         int(user_guess.text), message, feedback):
                        counting_guesses += 1
                        guess_title.set_text("Guess No. " + str(counting_guesses))
                mouse_up = True
        else:
            mouse_up = False

        # if not guess_button.is_clicked():
            # mouse_up = False

        for text_entry_field in all_text_entry_field:
            text_entry_field.draw(guessing_game_win)

        for button in all_buttons:
            button.draw(guessing_game_win)

        for label in all_labels:
            label.draw(guessing_game_win)

        pygame.display.update()
        await asyncio.sleep(0)

if __name__ == "__main__":
    app = run()
    asyncio.run(app)
