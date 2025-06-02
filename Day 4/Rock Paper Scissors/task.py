from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list1 = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for scissors:\n"))
if user_input not in [0,1,2]:
    print("Invalid Input!")

else:
    random_number = randint(0,2)
    if user_input == 0 and random_number == 2:
        print(f"{list1[0]}\n Computer chose:\n{list1[2]}\nYou win!")
    elif user_input == 1 and random_number == 0:
        print(f"{list1[1]}\n Computer chose:\n{list1[0]}\nYou win!")
    elif user_input == 2 and random_number == 1:
        print(f"{list1[2]}\n Computer chose:\n{list1[1]}\nYou win!")
    elif user_input == random_number:
        print(f"{list1[user_input]}\n Computer chose:\n{list1[random_number]}\nIt's a draw!")
    else:
        print(f"{list1[user_input]}\n Computer chose:\n{list1[random_number]}\nYou lose!")
