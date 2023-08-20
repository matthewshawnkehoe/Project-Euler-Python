'''
Project Euler : Problem 4
@author: Matthew Kehoe
'''
import time

start = time.time()

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def find_largest_palindrome(min=100,max=1000):
    result = 0
    for x in range(min, max):
        for y in range(min, max):
            z = x * y
            if is_palindrome(z) and z > result:
                result = z
    return result

val = find_largest_palindrome()

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))
