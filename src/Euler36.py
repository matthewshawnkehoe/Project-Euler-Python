'''
Project Euler : Problem 36
@author: Matthew Kehoe
'''
import time

start = time.time()


def convert_num_to_bin(num):
    bin_repr = bin(num)
    return bin_repr[2:]


def is_palindrome(num):
    return str(num) == str(num)[::-1]


sum = 0
for i in range(1, 1000000):
    b_ten_repr = i
    b_two_repr = convert_num_to_bin(i)
    if is_palindrome(b_ten_repr) and is_palindrome(b_two_repr):
        #print (b_ten_repr, b_two_repr)
        sum += b_ten_repr

val = sum

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))