'''
Project Euler : Problem 23
@author: Matthew Kehoe
'''
import functools
import time
start = time.time()

@functools.lru_cache(maxsize=None)
def sum_proper_divs(n):
    return sum(x for x in range(1, (n + 1) // 2 + 1) if n % x == 0 and n != x)

def is_abundant(num):
    if num < 12:
        return False
    return sum_proper_divs(num) > num

# List of abundant numbers
abundants = list(i for i in range(1, 28123) if is_abundant(i))

# Initialize a list of integers up to 28123
# We will zero out the locations where the index is the sum of two abundant numbers
non_abundants = [i for i in range(28123)]

# Calculate the sum of non abundant numbers by zeroing out every index which is the sum of two abundant numbers
# First, iterate through the amount of elements in the list of abundant numbers starting at index 1
for i in range(len(abundants)):
    # Then, iterate through every number from i to 28213 (the upper bound of non abundant numbers).
    for j in range(i, 28123):
        # If the sum of two abundant numbers is less than 28123, zero out the index of the sum
        if abundants[i] + abundants[j] < 28123:
            non_abundants[abundants[i] + abundants[j]] = 0
        else:
            break

val = sum(non_abundants)

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))