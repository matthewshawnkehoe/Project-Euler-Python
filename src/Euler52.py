'''
Project Euler : Problem 52
@author: Matthew Kehoe
'''
import time

start = time.time()

def same_digits(num):
  if sorted(str(num*6)) == sorted(str(num)):
    if sorted(str(num*5)) == sorted(str(num)):
      if sorted(str(num*4)) == sorted(str(num)):
        if sorted(str(num*3)) == sorted(str(num)):
          if sorted(str(num*2)) == sorted(str(num)):
            return True

val = 0
for i in range(1, 1000000):
  if same_digits(i) == True:
    val = i
    break

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))