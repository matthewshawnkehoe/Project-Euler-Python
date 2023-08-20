'''
Project Euler : Problem 20
@author: Matthew Kehoe
'''
import functools
import time
start = time.time()

@functools.lru_cache(maxsize=None)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

num = factorial(100)
str_num = str(num)
val = sum(int(i) for i in str_num)

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))