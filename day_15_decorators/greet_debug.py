def debug(func):
    def wrapper(*args, **kwargs):
        args_val = ", ".join(str(i) for i in args)
        kwargs_val = ", ".join(f"{k} = {v}" for k, v in kwargs.items())
        print(
            f"Calling function : {func.__name__} and args value: {args_val} and kwargs value {kwargs_val}"
        )
        return func(*args, **kwargs)

    return wrapper


@debug
def hello():
    return "Hello!!!"


@debug
def greet(name, greet="Hello"):
    return f"{greet}, {name}"


print(hello())
print(greet("Arpit", greet="Hi"))
