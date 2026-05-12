def is_prime(numb):
    if numb < 2:
        return False
    for i in range(2, numb):
        if numb % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(is_prime(int(input("Enter the number that you want to check for prime : "))))
