from itertools import chain, count
from math import sqrt

def isqrt(num):
    return int(sqrt(num))

def factors(num):
    return set(chain.from_iterable((i, num // i) for i in range(1, isqrt(num)) if num % i == 0))

def presents(num):
    return 10 * sum(factors(num))

def presents2(num):
    return 11 * sum(x for x in factors(num) if num / x <= 50)

def find_index(gen, f):
    return next(i for i, x in enumerate(gen) if f(x))

#print(find_index((presents(x) for x in count(0)), lambda x: x >= 36000000))
print(find_index((presents2(x) for x in count(0)), lambda x: x >= 36000000))