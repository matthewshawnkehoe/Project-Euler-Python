'''
Project Euler : Problem 7
@author: Matthew Kehoe
'''
import math
import time

start = time.time()

def isPrime(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return num > 1

my_list = []
my_list.append(2)
for n in range(3, 10000000):
    if len(my_list) > 10000:
        break
    if isPrime(n):
        my_list.append(n)

val = my_list[10000]

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))
