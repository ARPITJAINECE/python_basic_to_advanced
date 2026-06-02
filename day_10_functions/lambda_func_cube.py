import math

cube = lambda a: math.pow(a, 3)

cube_input = int(input("Enter the number to find its cube : "))
print(f"Cube of the number is : {cube(cube_input)}")
