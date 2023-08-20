'''
Project Euler : Problem 2
@author: Matthew Kehoe
'''
import time

start = time.time()

def fib(max=10):
    a = 1
    b = 2
    while a < max:
        yield a
        a, b = b, a + b


val = sum(i for i in fib(4000000) if i % 2 == 0)

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))

