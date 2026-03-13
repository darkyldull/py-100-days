##mycode

import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
word_list = ["aardvark", "baboon", "camel"]

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ["_"] * len(chosen_word)
print("".join(placeholder))

guess = ""

while "_" in placeholder and lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        print("Correct")
        for i in range(len(placeholder)):
            if guess == chosen_word[i]:
                placeholder[i] = guess
        print("".join(placeholder))

    else:
        print("Wrong")
        lives -= 1
        print(stages[lives])
    if lives == 0:
        print("You lose")
        break
if lives > 0:
    print("You win")

