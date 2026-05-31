def entry():
    return "Welcome to the number guessing game!!!"


def choose_level():
    print("Do you want hard level or easy level???")
    print("Press 'h' for hard and 'e' for easy")
    level = input("Enter your level type : ")
    return level


def hard_level():
    print("You have choosen hard level...\n Lets start game::::::")
    chances = 5
    print(f"You have {chances} left")

def easy_level():
    return "Hi"

if __name__ == "__main__":
    entry()
    choosen_level = choose_level()
    if choosen_level.lower() == "h":
        hard_level()
    elif choosen_level.lower() == "e":
        easy_level()
    else:
        print("Please enter correct value!!!")
