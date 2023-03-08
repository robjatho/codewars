import math


def is_square(n):
    if n >= 0:
        result = math.sqrt(n)
        if result.is_integer():
            return True

    return False
