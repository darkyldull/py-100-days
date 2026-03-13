from art import logo

print(logo)

bidding = {}

con = "yes"

def highest_bidder(bidding_dictionary):
    max_bid = 0
    winner = ""
    for key in bidding_dictionary:
        if bidding_dictionary[key] > max_bid:
            winner = key
            max_bid = bidding_dictionary[key]

    print(f"The winner is {winner} with {bidding_dictionary[winner]}")

while con.lower() == "yes":
    name = input("What is your name?: \n")
    bid = int(input("What is your bid?:\n"))
    bidding[name] = bid
    con = input("Are there more bidders?:\n")

highest_bidder(bidding)