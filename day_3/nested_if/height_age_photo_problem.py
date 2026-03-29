height = int(input("Enter the height in cm : "))
if height < 120:
    print("Cannot Ride")
else:
    bill = 0
    age = int(input("Enter your age : "))
    if age < 12:
        print("pay $5")
        bill = 5
    elif 12 > age < 18:
        print("pay $7")
        bill = 7
    else:
        print("pay $12")
        bill = 12
    wants_photo = input(
        "Do you want to take a photo ? ($3 will be charged extra)\nType Y for Yes or N for No : "
    )
    if wants_photo.upper() == "Y":
        bill += 3
print(f"Your total bill is : {bill}")
