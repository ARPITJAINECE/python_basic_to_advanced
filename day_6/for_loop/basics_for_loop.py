print("For loop practice !!!\n")
how_much = int(input("Enter the numbers that you will be entering ? "))
empty_list = []
for i in range(how_much):
    empty_list.append(int(input(f"Enter the {i+1} number : ")))

full_list = empty_list
print("\nYour list is : ", full_list)
