'''
Project Euler : Problem 38
@author: Matthew Kehoe
'''
import time

start = time.time()


def is_pandigital(num):
    num_str = str(num)
    length = len(num_str)
    s = ''.join(str(i) for i in range(1, length + 1))
    return ''.join(sorted(num_str)) == s


def multiply_by_nums(num):
    result = ''
    largest = 0
    for i in range(1, 6):
        result = result + str(num * i)
        if is_pandigital(result) and int(result) > largest:
            largest = int(result)
    return largest

# Generator which will return true if i generates the largest pandigital number
guess = [multiply_by_nums(i) for i in range(1, 100000)]

val = max(guess)

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))



