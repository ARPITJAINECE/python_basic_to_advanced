height = int(input("Enter the height in cm : "))
if height < 120:
    print("Cannot Ride")
else:
    age = int(input("Enter your age : "))
    if age < 12:
        print("pay $5")
    elif 12 > age < 18:
        print("pay $7")
    else:
        print("pay $12")
