'''
Project Euler : Problem 56
@author: Matthew Kehoe
'''
import time

start = time.time()

# Compute the digit sum
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

largest_sum = 0
for a in range(1, 101):
    for b in range(1, 101):
        digit_sum = sum_digits(a**b)
        if digit_sum > largest_sum:
            largest_sum = digit_sum

val = largest_sum

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))