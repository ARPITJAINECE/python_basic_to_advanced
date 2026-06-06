import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} seconds!!!")
        return result

    return wrapper


@timer
def exmaple_timer(timer_value):
    return time.sleep(timer_value)


exmaple_timer(5)
