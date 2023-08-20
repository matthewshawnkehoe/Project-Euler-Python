'''
Project Euler : Problem 16
@author: Matthew Kehoe
'''

import time
start = time.time()

num = 2**1000
str_num = str(num)
val = sum(int(i) for i in str_num)

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))