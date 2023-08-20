'''
Project Euler : Problem 30
@author: Matthew Kehoe
'''

import time

start = time.time()

def get_digits(num):
    while num > 0:
        digit = num % 10
        yield digit
        num = num // 10

# We only need to compute up until 1**5 + 2**5 + ... + 9**5 + 10**5
upper_bound = 1 + sum(i**5 for i in range(1, 11))

sum = 0
for i in range(2, upper_bound):
    digit_sum = 0
    total_digit_sum = 0
    digits = [j for j in get_digits(i)]
    # Go through all of the digits in the list and compute digit^5.
    # Combine all of the digit^5 in a total variable for every i.
    for d in digits:
        digit_sum += d ** 5
    total_digit_sum += digit_sum
    # If total = i, add i to the sum
    if i == total_digit_sum:
        sum += i

val = sum

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))