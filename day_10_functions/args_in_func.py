# sum_of_number = lambda *args: sum(args)
def sum_of_number(*args):
    # print(args)
    return sum(args)


print(f"sum is : {sum_of_number(1,2)}")
print(f"sum is : {sum_of_number(1,2,3)}")
print(f"sum is : {sum_of_number(1,2,3,4)}")
print(f"sum is : {sum_of_number(1,2,3,4,5)}")
print(f"sum is : {sum_of_number(1,2,3,4,5,6)}")
