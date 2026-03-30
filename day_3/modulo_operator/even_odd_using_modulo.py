number = int(input("Enter the number that you want to check (is its odd or even) ?\n"))
remainder = number % 2
if remainder == 0:
    print("even")
else:
    print("odd")

print("method 2 : ")
print("even" if remainder == 0 else "odd")
