print("Welcome to the Bidding System !!!!\n")
num_of_users = int(input("Enter the total number of users in this bidding : "))
empty_bidding_dict = {}
for num in range(num_of_users):
    name = input(f"Enter {num+1} player good Name : ")
    bid = int(input(f"Enter {num+1} bid value : "))
    print("\n")

    empty_bidding_dict[name] = bid

print(empty_bidding_dict)

max_bid = 0
winner_name = ""

names = list(empty_bidding_dict.keys())
bids = list(empty_bidding_dict.values())

for i in range(len(bids)):
    if bids[i] > max_bid:
        max_bid = bids[i]
        winner_name = names[i]

print(f"The winner name is : {winner_name} and the bid was : {max_bid}")
