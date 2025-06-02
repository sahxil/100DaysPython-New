# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from math import inf
#import os
import art

print(art.logo)
bidders = {}
more_bidders = "yes"

while more_bidders == "yes":
    name = input("What is your name?:\n")
    bid = int(input("What is your bid?:\n"))
    more_bidders = input("Are there any more bidders? Type 'yes' or 'no'.\n")
    bidders[name] = bid
    print("\n" * 20)

greatest_bid = -float(inf)
greatest_bidder = ""

for i in bidders:
    if bidders[i] > greatest_bid:
        greatest_bid = bidders[i]
        greatest_bidder = i

print(f"Greatest bidder is {greatest_bidder}")