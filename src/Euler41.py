'''
Project Euler : Problem 41
@author: Matthew Kehoe
'''
import functools
import time
from itertools import permutations

start = time.time()

@functools.lru_cache(maxsize=None)
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0 or n % (f+2) == 0:
            return False
        f += 6
    return True

'''
We can eliminate values by using the divisibility rule which states that an integer is divisible 
by 3 whose sum of digits is divisible by 3 and therefore composite and not prime.

For 123456789: 9+8+7+6+5+4+3+2+1 = 45, 45/3 = 15, NOT prime don't search nine digits
For 12345678: 8+7+6+5+4+3+2+1 = 36, 36/3 = 12, NOT prime don't search eight digits
For 1234567: 7+6+5+4+3+2+1 = 28, 28/3 = 9.333…, PRIME search seven digits
For 123456: 6+5+4+3+2+1 = 21, 21/3 = 7, NOT prime don't search six digits
For 12345: 5+4+3+2+1 = 15, 15/3 = 5, NOT prime don't search five digits
For 1234: 4+3+2+1 = 10, 4/3 = 1.333…, PRIME search four digits
...

This shows that only pandigital numbers of length 4 and 7 can form a prime number. Since we want 
the largest pandigital prime we’ll start with 7 digit numbers.

We need to search all seven digit numbers starting from 1234567 and ending at 7654321. It is safe 
to assume that a number between 7000000 and 7654321 will be prime by the prime number theorem.
'''

# Get the list of permutations for 1234567 and convert all elements to integers
perm = [int(''.join(p)) for p in permutations('1234567')]

list = [i for i in perm if is_prime(i)]

val = list[-1]

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))
