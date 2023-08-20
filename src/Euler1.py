'''
Project Euler : Problem 1
@author: Matthew Kehoe
'''
import time

start = time.time()

def sum_of_div_by_3_5(max=100):
    return(sum((i for i in range(1, max) if div_by_3_5(i))))

def div_by_3_5(x):
    return x % 3 == 0 or x % 5 ==0


val = sum_of_div_by_3_5(1000)

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))



