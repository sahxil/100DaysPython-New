import art
import random

print(art.logo)
print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
random_no = random.randint(1, 100)
#print(random_no)

difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard':")
no_of_tries = 5

if difficulty == "easy":
    no_of_tries = 10

for i in range(no_of_tries):
    guesses_left = no_of_tries - i
    print(f"You have {guesses_left} attempts remaining to guess the number.")
    guess = int(input("Make a guess:"))

    if guess > random_no and guesses_left != 1:
        print(f"Too high.\nGuess again.")
    elif guess < random_no and guesses_left != 1:
        print(f"Too low.\nGuess again.")
    elif guess == random_no and guesses_left != 1:
        print(f"You got it! the answer was {random_no}")
        break

    if guesses_left == 1:
        if guess == random_no:
            print(f"You got it! the answer was {random_no}")
        else:
            print("You've run out of guesses. Try again.")
