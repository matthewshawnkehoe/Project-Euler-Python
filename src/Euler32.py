'''
Project Euler : Problem 32
@author: Matthew Kehoe
'''

import time

start = time.time()

s = ''.join(str(i) for i in range(1, 10))

def is_pandigital(a, b, c):
    test = str(a) + str(b) + str(c)
    return ''.join(sorted(test)) == s

products = []
for x1 in range(1, 2000):
    for x2 in range(1, 100):
        if is_pandigital(x1, x2, x1 * x2):
            if x1 * x2 not in products:
                products.append(x1 * x2)
            print("%d: %d * %d" % (x1 * x2, x1, x2))

print(products)
val = sum(i for i in products)

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))

