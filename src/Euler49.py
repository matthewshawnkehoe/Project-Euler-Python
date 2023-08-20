'''
Project Euler : Problem 49
@author: Matthew Kehoe
'''
import itertools
import functools
import time
start = time.time()

elapsed = (time.time() - start)

# Make a list of all four digit prime numbers between 1000 and 10000
def get_primes():
    L = []
    for n in range(1000, 10000):
        if is_prime(n):
            L.append(n)
        else:
            continue
    return L

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

# Return all permutations of a number
def get_permutations(num):
    return list(map(''.join, itertools.permutations(str(num), 4)))

# Check if the arithmetic sequence are permutations of each other
def check_permutations(L, i, i1, i2):
    if (str(i1) in L) and (str(i2) in L):
        print(str(i), str(i1), str(i2), str(i) + str(i1) + str(i2))
        return str(i) + str(i1) + str(i2)


L = get_primes()
for i in L:
    for n in range(1, 3331):
        i1 = i + n
        i2 = (i + n) + n
        if is_prime(i1) and is_prime(i2):
            x = get_permutations(i)
            y = check_permutations(x, i, i1, i2)
            if y is not None:
                val = y
        else:
            continue


elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))