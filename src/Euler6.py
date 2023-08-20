'''
Project Euler : Problem 6
@author: Matthew Kehoe
'''
import time

start = time.time()

def sum_of_squares(num):
    total = 0
    for i in range(1, num+1):
        total += i ** 2
    return total

def square_of_sum(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total ** 2

val = square_of_sum(100) - sum_of_squares(100)

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))
