'''
Project Euler : Problem 35
@author: Matthew Kehoe
'''
import math
import functools
import time

start = time.time()

@functools.lru_cache(maxsize=None)
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def circular_prime(num):
    count = 0
    for i in rotation(num):
      if not is_prime(int(i)):
        break
      if is_prime(int(i)):
        count += 1
      if count == len(rotation(num)):
        return True

# Rotate the digits, not permute!
def rotation(n):
  rotations = set()
  for i in range( len( str(n) ) ):
    m = int( str(n)[i:] + str(n)[:i] )
    rotations.add(m)
  return rotations

val = sum(1 for i in range(2, 1000000) if (is_prime(i) and circular_prime(i)))

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))

