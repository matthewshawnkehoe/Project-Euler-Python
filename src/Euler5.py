'''
Project Euler : Problem 5
@author: Matthew Kehoe
'''
import time

start = time.time()

def isDivisible1to20(num):
    for i in [11, 13, 14, 16, 17, 18, 19, 20]:
        if num % i != 0:
            return False
    return True
# starting with number 1, check if it's divisible by 1 to 20
# we only need to check the even numbers as it has to be divisible by 20
# but, this means that we could start at the highest number which is 20
#
num = 20
while True:
    if isDivisible1to20(num):
        # if we've found the number, stop!
        break
    num += 20 # increment number

val = num

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))

