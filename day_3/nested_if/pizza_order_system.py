print("Welcome to the pizza delivery system!!!!\nPricing for Pizza is :")
print("On basis of Size : \n Small(S) : $15 \n Medium(M) : $20 \n Large(L) : $25")
print(
    "Price of adding pepperoni on basis of size : $2 for Small, $3 for Medium and $4 for Large"
)
print("Adding etxra cheese for any size : $1")
size = input("Which size pizza do you want ? (S, M or L)")
bill = 0
u_size = size.upper()
if u_size == "S":
    bill = 15
elif u_size == "M":
    bill = 20
elif u_size == "L":
    bill = 25
else:
    print("Invalid Size Selected")
pepperoni = input("Do you want peperoni or not ? (Y or N)")
if pepperoni.upper() == "Y":
    if u_size == "S":
        bill += 2
    elif u_size == "M":
        bill += 3
    elif u_size == "L":
        bill += 4
extra_cheese = input("Do you want extra cheese ? (Y or N)")
if extra_cheese.upper() == "Y":
    bill += 1

print(f"Your final bill is : {bill}")
