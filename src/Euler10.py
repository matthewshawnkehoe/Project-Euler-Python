'''
Project Euler : Problem 10
@author: Matthew Kehoe
'''
import math
import time

start = time.time()

def find_sum_of_primes(num=10):
    sum = 0
    for i in range(1, num):
        if is_prime(i):
            sum += i
    return sum

def is_prime(n):
    if n == 1:
        return False # 1 is a unit, not a prime

    # if n is even and not 2, then n isn't prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    # We only need to calculate up to the square root of n
    largest_divisor = math.floor(math.sqrt(n))

    # We can start from 3 and iterate by 2 to check all other odd numbers
    for x in range(3, largest_divisor + 1, 2):
        if n % x == 0:
            return False
    return True

val = find_sum_of_primes(2000000)

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))
