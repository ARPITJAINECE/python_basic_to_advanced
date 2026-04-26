student = {
    "name": input("enter your name : "),
    "roll": int(input("enter roll no : ")),
}
print(f"befor updating : {student}")

student["course"] = input("enter course : ")

print(f"after addition : {student}")

student["roll"] = 2

print(f"after updation : {student}")
