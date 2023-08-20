'''
Project Euler : Problem 26
@author: Matthew Kehoe
'''
import time
import math

start = time.time()

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

def generate_prime_below(n):
    listprimes = []
    for i in range(n, 1, -1):
        if is_prime(i):
            listprimes.append(i)

    return listprimes


# See https://math.stackexchange.com/questions/1502063/repeating-decimals-linked-to-reciprocals-of-primes
# In fact, if p is a prime greater than 5 (this excludes both primes 2 and 5 and also 3), the decimal expansion
# of 1/p is periodic with period length equals
#                                                 e = ord_p(10)
# the order of 10 modulo p, i.e., e is the smallest positive integer such that
#                                                 10^e ≡ 1(mod p)
# So, the length of the repeated part is 10^e(mod p) ≡ 1. The e can be (p-1) or a factor of (p-1).
for p in generate_prime_below(1000):
    e = 1
    # Start at e=1 and continue incrementing e
    while pow(10, e, p) != 1:
        e += 1
    # Stop when 10^e(mod p) ≡ 1 and e is (p-1) or a factor of (p-1). See Fermat's Little Theorem.
    if pow(10, e, p) == 1 and e == p - 1:
        break

val = p

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))