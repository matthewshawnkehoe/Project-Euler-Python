'''
Project Euler : Problem 3
@author: Matthew Kehoe
'''
import time

start = time.time()

def largestPrimeFactor(n):
    a = n
    b = 2
    while (a > b):
        if (a % b == 0):
            a = a / b
            b = 2
        else:
            b += 1
    print("Largest Prime Factor: %d" % (b))

val = largestPrimeFactor(600851475143)

elapsed = (time.time() - start)

print ("The prime factor was found in %s seconds" % (elapsed))

