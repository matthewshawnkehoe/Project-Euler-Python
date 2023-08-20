'''
Project Euler : Problem 14
@author: Matthew Kehoe
'''
import functools
import time
start = time.time()

@functools.lru_cache(maxsize=None)
def count_collatz(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        n = n / 2
        return 1 + count_collatz(n)
    n = 3*n + 1
    return 1 + count_collatz(n)

current_max_count = 0
current_max_num = 0
for i in range(1, 1000000):
    count = count_collatz(i)
    if count > current_max_count:
        current_max_count = count
        current_max_num = i

val = current_max_num

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))