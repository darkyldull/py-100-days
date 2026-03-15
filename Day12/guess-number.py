import random

def get_number():
    number_guess = random.randint(1, 100)
    return number_guess

def set_tries(difficulty):
    if difficulty.lower() == 'easy':
        return 10
    elif difficulty.lower() == 'hard':
        return 5
    else:
        print("Default difficulty = 10")
        return 10

def guess_number():
    return int(input("Make a guess: "))

def check_guess(tries, guess, actual_number):
    if guess == actual_number:
        print(f"You got it, the answer was {actual_number}")
        return tries, True
    elif guess > actual_number:
        print(f"Too high!")
        tries -= 1
        print(f"You have {tries} attempts left!")
        return tries, False
    else:
        print(f"Too low!")
        tries -= 1
        print(f"You have {tries} attempts left!")
        return tries, False

def game_start():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    actual_number = get_number()
    difficulty = input("Choose a difficulty. Type 'easy' or hard: ")
    tries = set_tries(difficulty)
    game_over = False
    while not game_over:
        guess = guess_number()
        tries, game_over = check_guess(tries, guess, actual_number)
        if tries == 0 and not game_over:
            game_over = True
            print(f"You lost, the number was {actual_number}")
    

    



game_start()