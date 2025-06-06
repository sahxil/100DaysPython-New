import art
from game_data import data
import random

print(art.logo)

def print_celebrities(celebA_dict, celebB_dict):
    print(f"Compare A: {celebA_dict['name']}, a {celebA_dict['description']}, from {celebA_dict['country']}")
    print(art.vs)
    print(f"Against B: {celebB_dict['name']}, a {celebB_dict['description']}, from {celebB_dict['country']}")

def pick_random_celeb():
    celeb1_dict = random.choice(data)
    return celeb1_dict

def check_followers(dict1, dict2):
    if dict1['follower_count'] > dict2['follower_count']:
        return "a"
    else:
        return "b"

current_score = 0
continue_game = True
celeb2 = pick_random_celeb()

while continue_game:
    celeb1 = celeb2
    celeb2 = pick_random_celeb()

    while celeb1 == celeb2:
        celeb2 = pick_random_celeb()

    print_celebrities(celeb1, celeb2)
    more_follower_celeb = check_followers(celeb1, celeb2)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if more_follower_celeb != guess:
        continue_game = False
    else:
        continue_game = True
        current_score += 1
        print(f"You're right! Current score: {current_score}.")

print(f"Sorry, that's wrong. Final score: {current_score}")
