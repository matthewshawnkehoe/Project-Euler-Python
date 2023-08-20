'''
Project Euler : Problem 21
@author: Matthew Kehoe
'''
import functools
import time
start = time.time()

@functools.lru_cache(maxsize=None)
def sum_proper_divs(n):
    return sum(x for x in range(1, (n + 1) // 2 + 1) if n % x == 0 and n != x)

# Let d(n) be defined as the sum of proper divisors of n
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
def amicable_nums(limit):
    for i in range(limit):
        j = sum_proper_divs(i)  # i = 220, j = sum_proper_divs(i) = 284, j = d(220) = d(i) = 284
        if i != j and sum_proper_divs(j) == i:  # Set i != j. We don't need to count i equals j twice.
            yield i  # True if i is equal to d(j). So, d(j_1 = 220) = i_1 = 284 and d(j_2 = 284) = i_2 = 220.
            # print(i) Uncomment if you want to see all the pairs found.

val = sum(amicable_nums(10000))

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))
