pic_file_name = "/Users/arpitjain/Desktop/python_learning/python_basic_to_advanced/day_16_file_handling/test_pic.jpg"
pic_copy_file_name = "/Users/arpitjain/Desktop/python_learning/python_basic_to_advanced/day_16_file_handling/test_pic_copy.jpg"
with open(pic_file_name, "rb") as f:
    source = f.read()
    f.close()

with open(pic_copy_file_name, "wb") as dest:
    dest.write(source)
    dest.close()
