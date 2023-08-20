'''
Project Euler : Problem 44
@author: Matthew Kehoe
'''
import time
start = time.time()

# Calculate the pentagon number
def pentagonNumber(n):
    return n*(3*n-1)//2

# Make a set of all the pentagon numbers
pentagonals = set(pentagonNumber(n) for n in range(1, 3000))

# Iterate through the set of pentagon numbers
difference = 0
for i in pentagonals:
    for j in pentagonals:
        if i != j:
            # Stop when we find a pair i and j which satisfy the sum and difference
            if abs(i + j) in pentagonals and abs(i - j) in pentagonals:
                difference = abs(i-j)

val = difference

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))