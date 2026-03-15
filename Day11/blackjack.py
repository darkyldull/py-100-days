import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def game_start():
    player = []
    computer = []
    game_status = False
    for i in range (0,2):
        draw_card(player)
        draw_card(computer)

    p_score = sum(player)
    c_score = sum(computer)
    print(f"Your cards: {player}, your sum: {p_score}")
    print(f"Computer's first card: {computer[0]}")
    return player, computer, p_score, c_score, game_status

def draw_card(hand):
    hand.append(random.choice(cards))
    if sum(hand) > 21 and 11 in hand:
        i = hand.index(11)
        hand[i] = 1

def hand_info(player, computer):
    print(f"Your cards: {player}, your score: {sum(player)}")
    print(f"Computer's hand: {computer[0]}")

def play_game():
    player, computer, p_score, c_score, game_over = game_start()
    while not game_over:
        if p_score == 21 or c_score == 21 or p_score > 21:
            game_over = True
        else:
            player_deal = input("Do you want to draw again? (Y/N): ")
            if player_deal.lower() == "y":
                draw_card(player)
                hand_info(player, computer)
                p_score = sum(player)
            else:
                game_over = True

    while c_score < 17:
        draw_card(computer)
        c_score = sum(computer)

    print(f"Your final hand: {player}, final score: {p_score}")
    print(f"Computer's final hand: {computer}, final score: {c_score}")

    if c_score == 21:
        print("You lose! Computer got a blackjack!")
    elif p_score == 21:
        print("You win! You got a blackjack!")
    elif c_score > 21:
        print("You win!, computer went over")
    elif p_score > 21:
        print("You lose!, you went over")
    elif c_score > p_score:
        print("You lose!, computer has a higher score")
    elif c_score < p_score:
        print("You win!, you have a higher score")
    elif c_score == p_score:
        print("Draw!")

while input("Do you want to play a game of blackjack? (Y/N): ").lower() == "y":
    play_game()







