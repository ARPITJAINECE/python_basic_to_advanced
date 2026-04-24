def life_in_weeks(age):
    diff = 90 - age
    op = diff * 52
    return op


inp = int(input("enter your age : "))
print(f"You have {life_in_weeks(inp)} weeks left.")
