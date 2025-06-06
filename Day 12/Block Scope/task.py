import math


def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return True
    else:
        length = int(math.sqrt(num))
        for i in range(3, length + 1):
            if num % i == 0:
                return False
        return True


is_prime(75)
