import random


def entry():
    return "Welcome to the number guessing game!!!"


def choose_level():
    print("Do you want hard level or easy level???")
    print("Press 'h' for hard and 'e' for easy")
    level = input("Enter your level type : ")
    return level


def hard_level(real_number):
    print("You have choosen hard level...\nLets start game::::::")
    chances = 5
    for i in range(chances, 0, -1):
        print(f"You have {i} chances left")
        input_number = int(input("Enter the number : "))
        if input_number < real_number:
            print("You have guessed lower number")
            print("Please try again...")
        elif input_number > real_number:
            print("You have entered big number")
            print("Please try again...")
        else:
            print("You have guessed correct number!!!")
            return
    print(f"Game Over! The number was {real_number}")


def easy_level(real_number):
    print("You have choosen easy level...\nLets start game::::::")
    chances = 10
    for i in range(chances, 0, -1):
        print(f"You have {i} chances left")
        input_number = int(input("Enter the number : "))
        if input_number < real_number:
            print("You have guessed lower number")
            print("Please try again...")
        elif input_number > real_number:
            print("You have entered big number")
            print("Please try again...")
        else:
            print("You have guessed correct number!!!")
            return
    print(f"Game Over! The number was {real_number}")


if __name__ == "__main__":
    entry()
    choosen_level = choose_level()
    real_number = random.randint(1, 100)
    if choosen_level.lower() == "h":
        hard_level(real_number)
    elif choosen_level.lower() == "e":
        easy_level(real_number)
    else:
        print("Please enter correct value!!!")
