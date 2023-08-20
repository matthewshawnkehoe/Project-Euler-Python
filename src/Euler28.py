'''
Project Euler : Problem 28
@author: Matthew Kehoe
'''

'''
21           25
    7     9 
       1  
    5     3 
17           13
'''

import time

start = time.time()

# Generate the numbers in the left diagonal including 1
def left_diagonal(n):
    side_length = 1
    number = 1
    while number < n:
        number += side_length - 1
        if number <= n:
            yield number
        side_length += 2

# Generate the numbers in the right diagonal excluding 1
def right_diagonal(n):
    side_length = 1
    number = 1
    while number < n:
        number += side_length * 2 + 2
        if number <= n:
            yield number
        number += side_length * 2 + 2
        if number <= n:
            yield number
        side_length += 2

left_diag = [i for i in left_diagonal(5*5)]
right_diag = [i for i in right_diagonal(5*5)]
print(left_diag)
print(right_diag)

print(sum(left_diag + right_diag))

left_diag2 = [i for i in left_diagonal(1001*1001)]
right_diag2 = [i for i in right_diagonal(1001*1001)]

val = sum(left_diag2 + right_diag2)

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))