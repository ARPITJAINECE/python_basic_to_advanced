file_name = "/Users/arpitjain/Desktop/python_learning/python_basic_to_advanced/day_16_file_handling/login.txt"

with open(file_name, "a") as f:
    f.write("user logged in at 10...\n")
    f.close()

with open(file_name, "a") as f:
    f.write("User logged in at 11 pm again...\n")
    f.close()

with open(file_name, "r") as f:
    content = f.read()
    print("Printing history of login's...\n")
    print(f"{content}")
    f.close()
