import random
import hangman_art
from hangman_art import stages
from hangman_words import word_list

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# TODO-2: - Update the code below to use the stages List from the file hangman_art.py
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
# TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#  e.g. You guessed d, that's not in the word. You lose a life.
# TODO-6: - Update the code below to tell the user how many lives they have left.
# TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.

print(hangman_art.logo)

chosen_word = random.choice(word_list)

"""All the comments below this are essential for dry run purposes hence not deleted"""

#print(chosen_word)

lives = 6

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
#print(placeholder)

display = list(placeholder)

wrong_guesses = ""
right_guesses = ""

while "_" in display and lives != 0:
    print(f"****************************{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        if guess not in right_guesses:
            right_guesses += guess
            for i in range(len(chosen_word)):

                if chosen_word[i] == guess:
                    display[i] = guess

            print("".join(display))

        else:
            print(f"You've already guessed {guess} before")

    else:
        if guess not in wrong_guesses:
            wrong_guesses += guess
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")

        else:
            print(f"You've already guessed {guess} before")

        print("".join(display))

    #print(lives)
    print(stages[6 - lives])

if lives != 0:
    print("****************************YOU WIN****************************")
else:
    print(f"***********************YOU LOSE**********************")
    print("The correct word is "+chosen_word)