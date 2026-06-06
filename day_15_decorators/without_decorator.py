def my_decorator(func):
    def wrapper():
        print("Dec Started")
        func()
        print("Dec Stopped")

    return wrapper


def hello():
    print("Hi , Hello!!!!")


hello = my_decorator(hello)

hello()
