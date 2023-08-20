'''
Project Euler : Problem 25
@author: Matthew Kehoe
'''
import functools
import time
start = time.time()

@functools.lru_cache(maxsize=None)
def Fibonacci(n):
    # Make the first term, F_1 = 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)

# Start at 1 and increment by 1 to see which number has 1000 digits
num = 1
while len(str(Fibonacci(num))) != 1000:
   num += 1

val = num

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))
