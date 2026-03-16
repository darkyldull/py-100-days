import random
from game_data import data

def get_comparison():
    choice_1 = random.choice(data)
    choice_2 = random.choice(data)
    while choice_1 == choice_2:
        choice_2 = random.choice(data)

    return choice_1, choice_2

def print_information(choice1, choice2):
    print(f"Compare A: {choice1['name']}, a/an {choice1['description']}, from {choice1['country']}")
    print("VS")
    print(f"Against B: {choice2['name']}, a/an {choice2['description']}, from {choice2['country']}")
    
def compare_followers(user_choice, choice_1, choice_2):
    if user_choice == 'A' and int(choice_1['follower_count']) > int(choice_2['follower_count']):
        print("Correct!")
        return False
    elif user_choice == 'B' and int(choice_1['follower_count']) < int(choice_2['follower_count']):
        print("Correct!")
        return False
    else:
        print("Wrong!")
        print(f"{choice_1['name']}, {choice_1['follower_count']} and {choice_2['name']}, {choice_2['follower_count']}")
        return True

def game_start():
    score = 0
    game_over = False
    while not game_over:
        choice_1, choice_2 = get_comparison()
        print_information(choice_1, choice_2)
        user_choice = input("Who has more followers, A or B? ")
        game_over = compare_followers(user_choice, choice_1, choice_2)
        if not game_over:
            score += 1
            print(f"You are correct, score is {score}")
            print("===================================")
    print("===================================")
    print(f"Final score: {score}")

game_start()

