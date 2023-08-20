'''
Project Euler : Problem 48
@author: Matthew Kehoe
'''
import time
start = time.time()

val = sum(i**i for i in range(1, 1001)) % 10000000000

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))