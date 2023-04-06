import os

from art import logo

print(logo)
print("Welcome to the secret auction program.")

all_bids = {}


def check_highest_bid(bids):
    highest_bid = 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
    print(f"The winner is {bidder} with a bid of ${highest_bid}")


more_bidders_exists = True
while more_bidders_exists:
    username = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    all_bids[username] = bid_amount

    more_bidders = input("Are there any other bidders? type 'yes' or 'no'. \n")
    if more_bidders == "yes":
        os.system('cls')
    else:
        more_bidders_exists = False
        check_highest_bid(all_bids)
