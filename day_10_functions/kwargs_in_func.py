def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


print_kwargs(name="a", age=1)
print_kwargs(name="b")
print_kwargs(name="a", age=1, home="jpr")
