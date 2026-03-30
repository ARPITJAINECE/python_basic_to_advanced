height = int(input("Enter the height in cm : "))
if height < 120:
    print("Cannot Ride")
else:
    bill = 0
    age = int(input("Enter your age : "))
    if 45 <= age <= 55:
        print("Everything is going to be OK, Get a FREE-RIDE from us !!!!!")
        bill = 0
        wants_photo = "N/A"
    elif age < 12:
        print("pay $5")
        bill = 5
    elif 12 > age < 18:
        print("pay $7")
        bill = 7
    else:
        print("pay $12")
        bill = 12
    if not (45 <= age <= 55):
        wants_photo = input("Do you want to take a photo? ($3 extra) Y or N: ")
        if wants_photo.upper() == "Y":
            bill += 3
    else:
        print("Your free photo has been added to your session.")
print(f"Your total bill is : {bill}")
