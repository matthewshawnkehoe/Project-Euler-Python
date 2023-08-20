'''
Project Euler : Problem 53
@author: Matthew Kehoe
'''
import math
import time

start = time.time()

def nCr(n, r):
    f = math.factorial
    return f(n) // (f(r) * f(n-r))

counter = 0
for n in range(1, 101):
  for r in range(1, 101):
    if n > r and nCr(n, r) > 1000000:
      counter += 1

val = counter

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))