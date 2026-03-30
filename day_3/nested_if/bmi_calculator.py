# If the bmi is under 18.5 (not including), print out "underweight"

# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

# If the bmi is 25 (including) or over, print out "overweight"

weight = float(input("enter your weight : "))
height = float(input("enter your height : "))
bmi = weight / (height**2)
if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi > 25:
    print("normal weight")
else:
    print("overweight")
