'''
Project Euler : Problem 27
@author: Matthew Kehoe
'''
import time
import math
import functools

start = time.time()

@functools.lru_cache(maxsize=None)
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

# Generate all of the primes produced from n**2 + a*n + b
def quadratic_primes(a, b):
    n = 0
    val = abs(n**2 + a*n + b)
    prime = is_prime(val)
    while prime:
        yield val
        n += 1
        val = abs(n**2 + a*n + b)
        prime = is_prime(val)


# Tuple to store the coefficients a and b from n**2 + a*n + b.
# Also stores the length of the quadratic primes list generated.
# Format (a, b, len(quadratic_primes_list))
current_longest = (0, 0, 0)

# Loop through abs(a) < 1000 and abs(b) <= 1000
# We only need to check the values where a and b are prime (insert mathematical reason why)
for a in range(-999, 1000):
    if not is_prime(abs(a)):
        continue
    for b in range(-1000, 1000):
        if not is_prime(abs(b)):
            continue
        # Generate a list of primes from a to b.
        primes = [p for p in quadratic_primes(a, b)]
        if len(primes) > current_longest[2]:
            # If the length of the list of primes between a and b is greatest, make current longest
            # the new a and b.
            current_longest = (a, b, len(primes))

print (current_longest)
# We need to return a * b which is stored inside the first two slots of the tuple.
val = current_longest[0] * current_longest[1]

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))