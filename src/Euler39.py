'''
Project Euler : Problem 39
@author: Matthew Kehoe
'''
import time

start = time.time()


def findNumSoln(p):
    for a in range(1, p // 2):
        aSquared = a ** 2
        # Assume b is the larger side
        for b in range(a, p // 2):
            bSquared = b ** 2
            # There is no reason to make a separate loop for c
            # The condition is only satisfied if a + b + c = p
            # a ** 2 + b ** 2 = c ** 2 must also be satisfied
            c = p - (a + b)
            cSquared = c ** 2
            if aSquared + bSquared == cSquared:
                yield a, b, c
            elif aSquared + bSquared > cSquared:
                break


def int_right_tri(p):
    return {tuple(sorted(i)) for i in findNumSoln(p)}


list = [len(int_right_tri(i)) for i in range(1, 1001)]

# Return the value of p which has the highest number of solutions.
# Note that the index starts at 0.
val = list.index(max(list)) + 1

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))
