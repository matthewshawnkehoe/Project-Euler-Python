'''
Project Euler : Problem 43
@author: Matthew Kehoe
'''
import time
from itertools import permutations
start = time.time()

# Get the list of permutations for 0123456789 and convert all elements to strings
perm = [str(''.join(p)) for p in permutations('0123456789')]

# Create a variable for the sum
sum = 0

# Search through all permutations of 0123456789 and add to sum those which satisfy the given constraints
for p in perm:
    if (int(p[7:10]) % 17 == 0 and
        int(p[6:9]) % 13 == 0 and
        int(p[5:8]) % 11 == 0 and
        int(p[4:7]) % 7 == 0 and
        int(p[3:6]) % 5 == 0 and
        int(p[2:5]) % 3 == 0 and
        int(p[1:4]) % 2 == 0):
        sum += int(p)

val = sum

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))
