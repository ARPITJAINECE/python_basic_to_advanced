def input_from_user():
    inp = int(input("Enter the Year : "))
    return inp


def leap_checker(year):
    if year % 400 == 0 and year % 4 == 0:
        # print(f"{year} is a leap year..")
        return True
    elif year % 100 == 0:
        # print(f"{year} is not a leap year..")
        return False
    else:
        # print(f"{year} is not a leap year..")
        return False


if __name__ == "__main__":
    print("Welcome to the LEAP YEAR finder!!")

    year_inp = input_from_user()

    print(leap_checker(year_inp))
