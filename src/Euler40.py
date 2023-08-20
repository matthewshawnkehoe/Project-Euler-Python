'''
Project Euler : Problem 40
@author: Matthew Kehoe
'''
import time

start = time.time()

# Create a generator to yield all of the integers up to n.
def up_to_num(n):
    num = 0
    while num < n:
        yield num
        num += 1

# Convert the generator to a list of numbers.
list_of_num = [i for i in up_to_num(1000001)]

# Convert this list to an integer
num_str = "".join(str(i) for i in list_of_num)

# Calculate d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
val = int(num_str[1]) * int(num_str[10]) * int(num_str[100]) * int(num_str[1000]) * \
      int(num_str[10000]) * int(num_str[100000]) * int(num_str[1000000])

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))
