'''
Project Euler : Problem 9
@author: Matthew Kehoe
'''
import math
import time

start = time.time()


def find_pythagorean_triplet(num=100):
    for a in range(1, num):
        for b in range(1, num):
            c = math.sqrt(a**2 + b**2)
            if a + b + c == num:
                return a * b * c

val = int(find_pythagorean_triplet(1000))

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))
