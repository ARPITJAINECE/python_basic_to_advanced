file_name = "/Users/arpitjain/Desktop/python_learning/python_basic_to_advanced/day_16_file_handling/myfile_write.txt"

with open(file_name, "w") as f:
    print("Started writing in a file.....")
    f.write("This is my content 1...\n")
    f.write("This is my content 2...")
    # f.close()

with open(file_name, "r") as f:
    content = f.read()
    print("printing file content....")
    print(content)
    # f.close()

# if using with block, then closing of file is not need, because its been taken care after with block completes.
