import random
from myGuessingGameGUI import GREEN


def input_range(p_min_input_field, p_max_input_field, p_message):
    users_min_range = int(p_min_input_field)
    users_max_range = int(p_max_input_field)

    if users_min_range < users_max_range:
        # print("The range you selected is: %d - %d" % (users_min_range, users_max_range))
        chances_of_success = users_max_range - users_min_range + 1
        #print("You have a 1 to %d chances of success" % chances_of_success)

        message_output = ("The range you selected is: %d - %d"
                          "You have a 1 to %d chances of success"
                          %(users_min_range, users_max_range, chances_of_success))
        p_message.set_text(message_output)
        return generate_random(users_min_range, users_max_range)
    else:
        message_output = "The max number is larger than the min number. Please choose the numbers again"
        p_message.set_text(message_output)
        # print("The max number is larger than the min number. Please choose the numbers again")
        # input_range()



def generate_random(p_min_number, p_max_number):
    random_number = random.randint(p_min_number, p_max_number)
    return random_number
    # print("The number selected is: %d" % random_number)

    # time_to_guess(random_number, p_min_number, p_max_number)


def time_to_guess(p_number_to_guess, p_min_number, p_max_number, p_user_guess, p_message, p_feedback):
    # user_guess = None
    # counting_guesses = 1

    while p_user_guess != p_number_to_guess:
        # print("\nGuess No. %d :" % counting_guesses)
        # user_guess = int(input("Guess the number selected: "))

        if p_user_guess < p_min_number or p_user_guess > p_max_number:
            p_message.set_text("Please select a number within the range")
            # print("Please select a number within the range")
            # time_to_guess(p_number_to_guess, p_min_number, p_max_number)
        else:
            if p_user_guess > p_number_to_guess:
                p_feedback.set_text("The number you selected is larger than the chosen number")
                # print("The number you selected is larger than the chosen number")

            elif p_user_guess < p_number_to_guess:
                p_feedback.set_text("The number you selected is smaller than the chosen number")
                # print("The number you selected is smaller than the chosen number")
        return False
            # counting_guesses = counting_guesses + 1
    p_feedback.set_color(GREEN)
    p_feedback.set_text("Congratulations, you guessed the number")
    return True

    # print("Congratulations, you guessed the number\n"*2)
    # crack_the_code()


def crack_the_code():
    guessed_word = input("You have one more task...\nTry to guess the following word: *i*ne*\nGuess No.1:\n")
    counting_guesses = 2

    while guessed_word != "winner":
        print("\nGuess No. %d :" % counting_guesses)
        guessed_word = input("Please try again \n")
        counting_guesses = counting_guesses + 1
    print("Congratulations, you guessed the word")


def request_user_name(p_user_name):
    if p_user_name != "":
        return "Welcome %s" % p_user_name
    else:
        return "Please enter your name"
    # user_name = input("Please enter your name here: ")
    # print("Your name is: " + user_name)


# input_range()
# request_user_name()
