# testing1234
# imports
# imports random module
import random

# this function creates a random number based on the two numbers the user chose
def random_numbers(min_num, max_num):
    return random.randint(min_num, max_num)


# this function checks to see if the input is a number
def is_a_number(msg):
    user = input(msg)
    while not user.isdigit():
        user = input(msg)
    return int(user)


# this function checks to see if the second number is lower then the first number
def is_num_less(user, value):
    while user <= value:
        return is_a_number("Choose a higher number: ")


def restart_game():
    choice = input("You only have two choices! P or Q: ")
    while choice != "p" and choice != "q":
        choice = input("You only have two choices! p or q!: ")
    return choice == "p"


# this function starts the game
def start_game(game):

    while game:
        # gets the user inputs
        user_min_num = is_a_number("Please provide a low number: ")
        user_max_num = is_a_number("Please Provide a high number: ")

        # check if the high number is lower then the lower number
        while user_max_num <= user_min_num:
            user_max_num = is_num_less(user_max_num, user_min_num)

        # generates a random number
        random_number = random_numbers(user_min_num, user_max_num)

        # the user guesses the random number that was generated
        guess = is_a_number("Guess the number that was generated: ")
        # checks to see if the guessed number matches the random number that was generated
        while guess != random_number:
            # if the number is to high then it will inform the user
            if guess < random_number:
                guess = is_a_number("That choice is to low: ")
            # if the number is to low then it will inform the user
            else:
                guess = is_a_number("That was choice was to high: ")
        # announces that the user has won the number guessing game
        print(f"Congratulations your choice of {guess} was correct!")
        # restarts the game
        game = restart_game()


# starts the game when the script is loaded
start_game(True)