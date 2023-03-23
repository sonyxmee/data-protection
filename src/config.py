import math
import random


def get_simple_number(p_, q_):
    n = p_ * q_
    f = (p_ - 1) * (q_ - 1)
    a = random.randint(0, n)
    while math.gcd(a, f) != 1:
        a = random.randint(0, n)
    return a


# def is_simple(p_, q_):
#     if math.gcd(p, q) == 1:
#         return True
#     return False


# def get_simple_numbers():
#     a = random.randint(1, 100)
#     b = random.randint(1, 100)
#
#     while math.gcd(a, b) != 1:
#         a = random.randint(1, 100)
#         b = random.randint(1, 100)
#     return a, b

p = 7
q = 13
e = get_simple_number(p, q)
