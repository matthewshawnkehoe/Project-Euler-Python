'''
Project Euler : Problem 24
@author: Matthew Kehoe
'''
import itertools
import time
start = time.time()

# Apply the built-in permutations within itertools
list_lex_perm = list(map("".join, itertools.permutations('0123456789', 10)))
# return the millionth lexicographic permutation, the index starts at 0
val = list_lex_perm[1000000 - 1]

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))
