'''
Project Euler : Problem 29
@author: Matthew Kehoe
'''

import time

start = time.time()

def power(a, b):
    yield a**b

list = []
def generate_list(a, b):
    for x in range(a, b):
        for y in range(a, b):
            next_ele = [i for i in power(x, y)]
            if next_ele not in list:
                list.append(next_ele)
    return len(list)


val = generate_list(2, 101)

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))