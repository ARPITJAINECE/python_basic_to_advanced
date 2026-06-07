file_name = "/Users/arpitjain/Desktop/python_learning/python_basic_to_advanced/day_16_file_handling/test_binary.bin"
with open(file_name, "wb") as f:
    data = bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    f.write(data)

with open(file_name, "rb") as f:
    raw_data = f.read()
    print(f"{raw_data}")
    # decoded_data = raw_data.decode("utf-8")
    decoded_data = list(raw_data)
    print(f"decoded data is : {decoded_data}")
    f.close()
