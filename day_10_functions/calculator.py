def enter_number(inp):
    num = input(f"Enter the {inp} number : ")
    if num.isalpha():
        print(f"Wrong Input of {inp} number ...")
        return
    else:
        return float(num)


def pick_operand():
    list_operation = ["+", "-", "*", "/", "%"]
    for i in range(len(list_operation)):
        print(list_operation[i])

    choice = input("Enter your choice : ")

    if choice in list_operation:
        return choice
    else:
        print("Invalid Operation selected!!!")
        return None


def calculation(first, operand, second):
    if operand == "+":
        return first + second
    elif operand == "-":
        return first - second
    elif operand == "*":
        return first * second
    elif operand == "/":
        if second == 0:
            return "Error : Cannot / by 0"
        else:
            return first / second
    else:
        return first % second


if __name__ == "__main__":
    print("Welcome to Calculator!!!!")
    first_number = enter_number("first")
    continue_again = True

    while continue_again:

        if first_number is not None:
            operation = pick_operand()

            if operation is not None:
                second_number = enter_number("second")

                if second_number is not None:
                    final = calculation(first_number, operation, second_number)
                    print(f"{first_number} {operation} {second_number} = {final}")

                    print(
                        f"\nType y to use {final} as your new continuing first number now OR Type n to start new calculations OR Type e to exit : "
                    )
                    user_choice_input = input("Enter your choice : ")

                    if user_choice_input == "y" or user_choice_input == "Y":
                        first_number = final
                    elif user_choice_input == "n" or user_choice_input == "N":
                        print("Starting new calculations")
                        first_number = enter_number("first")
                    else:
                        print("Wrong Choice, Exiting")
                        continue_again = False
                else:
                    break
            else:
                break
        else:
            break
