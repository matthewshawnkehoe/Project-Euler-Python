'''
Project Euler : Problem 31
@author: Matthew Kehoe
'''

import time

start = time.time()
number_of_ways = 0

# Brute force approach, we could apply dynamic programming.
# Iterate over every coin of value
# a = one pence = 1
# b = two pence = 2
# c = five pence = 5
# d = ten pence = 10
# e = twenty pence = 20
# f = fifty pence = 50
# g = one pound = 100
# h = two pounds = 200
# and observe that we should solve
# a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100 + h*200 = 200
# We can reduce the running time by inserting break statements as constructed.

for a in range(0, 201):
    if a*1 > 200:
        break
    for b in range(0, 101):
        if a*1 + b*2 > 200:
            break
        for c in range(0, 41):
            if a*1 + b*2 + c*5 > 200:
                break
            for d in range(0, 21):
                if a*1 + b*2 + c*5 + d*10 > 200:
                    break
                for e in range(0, 11):
                    if a*1 + b*2 + c*5 + d*10 + e*20 > 200:
                        break
                    for f in range(0, 5):
                        if a*1 + b*2 + c*5 + d*10 + e*20 + f*50 > 200:
                            break
                        for g in range(0, 3):
                            if a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100 > 200:
                                break
                            for h in range(0, 2):
                                if (a*1 + b*2 + c*5 + d*10 + e*20 + f*50 + g*100 + h*200) == 200:
                                    number_of_ways += 1

val = number_of_ways

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))

