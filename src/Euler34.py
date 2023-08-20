'''
Project Euler : Problem 34
@author: Matthew Kehoe
'''
import time
import functools

start = time.time()


@functools.lru_cache(maxsize=None)
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


def get_digits(num):
    while num > 0:
        digit = num % 10
        yield digit
        num = num // 10


def equal_to_sum_fact_digts(num):
    digit_sum = 0
    total_digit_sum = 0
    digits = [j for j in get_digits(num)]
    for d in digits:
        digit_sum += factorial(d)
    total_digit_sum += digit_sum
    return total_digit_sum


list = []
for i in range(3, 100000):
    if equal_to_sum_fact_digts(i) == i:
        list.append(i)

print(list)

val = (sum(i for i in list))

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))





