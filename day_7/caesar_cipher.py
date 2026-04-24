input_from_user = input("Enter the word : ")
char_array = list(input_from_user)
print(char_array)
empty_ascii = []
for char in char_array:
    ascii_value = ord(char)
    empty_ascii.append(ascii_value)

print(empty_ascii)
shiftings = int(input("Enter the number  of shiftings you will be needing : "))
after_shift_ascii = []
for each_ascii in empty_ascii:
    after_shift_ascii.append(each_ascii + shiftings)

print(after_shift_ascii)

after_shift_char = []
for each_after_shift in after_shift_ascii:
    after_shift_char.append(chr(each_after_shift))

print(after_shift_char)
