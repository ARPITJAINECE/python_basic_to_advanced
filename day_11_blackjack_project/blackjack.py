import random


def deck_cards():
    return [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards(cards):
    return random.choice(cards)


def cal_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(sum_player,sum_comp):
    if sum_player>21 and sum_comp>21:
        return "Your SUM exceeded, GAME OVER!!!"
    
    if sum_player==sum_comp:
        return "DRAW"
    elif 


if __name__ == "__main__":
    print("Welcome to BlackJack game!!!")
    cards = deck_cards()
    # print(cards)
    player_cards = []
    computer_cards = []
    for _ in range(2):
        player_cards.append(deal_cards(cards))
        computer_cards.append(deal_cards(cards))

    # print(f"player cards : {player_cards}")
    # print(f"computer cards : {computer_cards}")

    game_over = False
    while not game_over:

        sum_player = cal_score(player_cards)
        sum_comp = cal_score(computer_cards)

        # print(f"player cards sum : {sum_player}")
        # print(f"comp cards sum : {sum_comp}")

        print(f"Your cards are : {player_cards} and your total sum is : {sum_player}")
        print(f"Computer cards sum is : {sum_comp}")

        if sum_player == 0 or sum_comp == 0 or sum_player > 21:
            print("Your cards sum > 21, GAME OVER!!!")
            game_over = True
        else:
            user_next_input = input("Type 'y' to get another card or 'n' to pass : ")
            if user_next_input == "y" or user_next_input == "Y":
                player_cards.append(deal_cards(cards))
            else:
                game_over = True
