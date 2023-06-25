import random

stages = ['''
    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
==========
''', '''
    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
==========
''','''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
==========
   ''','''
   +---+
    |   |
    0   |
   /|   |
        |
        |
==========
''','''
    +---+
    |   |
    0   |
    |   |
        |
        |
==========
''','''
    +---+
    |   |
    0   |
        |
        |
        |
==========
''','''
    +---+
    |   |
        |
        |
        |
        |
==========
''']
word_list = ["ardvark", "baboon", "camel", "elephant","lion","chetta","giraffe"]
chosen_word= random.choice(word_list)
word_length = len(chosen_word)

lives = 6
display = []
print(f"pls, the solution is {chosen_word}.")


for _ in range(word_length):
    display += "_"
    print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
if guess not in chosen_word:
    lives -= 1
    if lives == 0:
        end_of_game = True
        print("You lose.")
print(f"{' ' .join(display)}")
if "_" not in display:
    end_of_game = True
    print("You wins!")