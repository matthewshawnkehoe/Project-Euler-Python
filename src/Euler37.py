'''
Project Euler : Problem 37
@author: Matthew Kehoe
'''
import functools
import time
import math

start = time.time()


@functools.lru_cache(maxsize=None)
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


# Not used but can be referenced to check if is_truncatable_left_to_right.
def is_truncatable_left_to_right(num):
    #print(num)
    num_str = str(num)
    while len(num_str) > 1:
        if not is_prime(num):
            return False
        if is_prime(num):
            if not is_prime(int(num_str[1:])):
                return False
            num_str = num_str[1:]
            #print(num_str)
    return True


# Not used but can be referenced to check if is_truncatable_right_to_left.
def is_truncatable_right_to_left(num):
    #print(num)
    num_str = str(num)
    while len(num_str) > 1:
        if not is_prime(num):
            return False
        if is_prime(num):
            if not is_prime(int(num_str[:-1])):
                return False
            num_str = num_str[:-1]
            #print(num_str)
    return True


def check_truncatable_primes(num):
    num_str1 = str(num)
    num_str2 = str(num)
    while len(num_str1) > 1 or len(num_str2) > 1:
        if not is_prime(num):
            return False
        if is_prime(num):
            if not is_prime(int(num_str1[1:])):
                return False
            num_str1 = num_str1[1:]
            if not is_prime(int(num_str2[:-1])):
                return False
            num_str2 = num_str2[:-1]
    return True


val = sum(i for i in range(10, 800000) if (check_truncatable_primes(i)))

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))

