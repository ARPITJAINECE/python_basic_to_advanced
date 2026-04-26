student = {
    "name": "arpit jain",
    "roll no": 10,
    "city": "jaipur",
}

print("only keys")
# only over keys
for key in student:
    print(f"{key}")

print("only values")
# only over values
for value in student.values():
    print(f"{value}")

print("both keys and values")
# both k-v pairs
for key, value in student.items():
    print(f"{key}: {value}")
