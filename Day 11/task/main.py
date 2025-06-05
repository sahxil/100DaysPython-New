import random
import art

game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if game_start == "y":
    print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def print_final_output(uu_list, dd_list):
    print(f"Your final hand: {uu_list}, final score: {sum(uu_list)}")
    print(f"Computer's final hand: {dd_list}, final score: {sum(dd_list)}")

def check_who_wins(u_list, d_list):
    if sum(u_list) > 21:
        print_final_output(u_list, d_list)
        print("You went over, you lose")

    elif sum(d_list) > 21:
        print_final_output(u_list, d_list)
        print("Opponent went over, you WIN!")

    else:
        if sum(u_list) > sum(d_list):
            print_final_output(u_list, d_list)
            print("You win")

        elif sum(u_list) < sum(d_list):
            print_final_output(u_list, d_list)
            print("You lose")

        else:
            print_final_output(u_list, d_list)
            print("DRAW")


while game_start == "y":

    users_cards = []
    dealer_cards = []

    for i in range(2):
        card_generated = random.choice(cards)
        print(card_generated)
        users_cards.append(card_generated)

    temp_card_generated = random.choice(cards)
    print(temp_card_generated)
    dealer_cards.append(temp_card_generated)

    user_score = sum(users_cards)
    dealer_score = sum(dealer_cards)

    if user_score == 22:
        users_cards[1] = 1
        user_score = sum(users_cards)

    if user_score == 21:
        print(f"Your final hand: {users_cards}, final score: {user_score}")
        print(f"Computer's final hand: {dealer_cards[0]}, final score: {dealer_score}")
        print("BLACKJACK. You WIN!")

    else:
        print(f"Your cards: {users_cards}, current score: {user_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

    continue_game = input("Type 'y' to get another card, type 'n' to pass: ")

    while continue_game == "y" and user_score <= 21:
        card_generated = random.choice(cards)
        print(card_generated)
        if card_generated == 11:
            if user_score < 11:
                users_cards.append(card_generated)
            else:
                card_generated = 1
                users_cards.append(card_generated)
        else:
            users_cards.append(card_generated)

        user_score = sum(users_cards)

        print(f"Your cards: {users_cards}, current score: {user_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if user_score > 21:
            break

        continue_game = input("Type 'y' to get another card, type 'n' to pass: ")

    if continue_game == "n":
        while dealer_score <= 16:
            card_generated = random.choice(cards)
            print(card_generated)
            if card_generated == 11:
                if dealer_score < 11:
                    dealer_cards.append(card_generated)
                else:
                    card_generated = 1
                    dealer_cards.append(card_generated)
            else:
                dealer_cards.append(card_generated)

            dealer_score = sum(dealer_cards)

    check_who_wins(users_cards, dealer_cards)

    game_start = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':")