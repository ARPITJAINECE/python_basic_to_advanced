import time


def cache(func):
    cache_value = {}
    print(f"Cache value is {cache_value}")

    def wrapper(*args, **kwargs):
        if args in cache_value:
            return cache_value[args]
        result = func(*args, **kwargs)
        cache_value[args] = result
        print(f"Cache value is {cache_value}")
        return result

    return wrapper


@cache
def long_func(a=1, b=2):
    time.sleep(1)
    return a + b


print(long_func(2, 3))
print(long_func(3, 4))
print(long_func(2, 3))
print(long_func(2, 3))
print(long_func())
print(long_func(b=1, a=7))
