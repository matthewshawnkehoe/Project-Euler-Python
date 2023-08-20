'''
Project Euler : Problem 15
@author: Matthew Kehoe
'''

import functools
import time
start = time.time()

@functools.lru_cache(maxsize=None)
# the x-coordinate is the abscissa and the y-coordinate is the ordinate
def paths(abscissa, ordinate, max_abscissa, max_ordinate):
    # if at bottom right of grid, return 1 (base case)
    if abscissa == max_abscissa and ordinate == max_ordinate:
        return 1
    # if at highest x value, go down 1
    if abscissa == max_abscissa:
        return paths(abscissa, ordinate + 1, max_abscissa, max_ordinate)
    # if at lowest y value, go right 1
    if ordinate == max_ordinate:
        return paths(abscissa + 1, ordinate, max_abscissa, max_ordinate)
    # else wise go right 1 and down 1
    return paths(abscissa + 1, ordinate, max_abscissa, max_ordinate) + \
           paths(abscissa, ordinate + 1, max_abscissa, max_ordinate)

val = paths(0,0,20,20)

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))