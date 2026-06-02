def factorial(number):
    if number != 0:
        return number * factorial(number - 1)
    else:
        return 1


print(f"factorial of 5 is : {factorial(5)}")
