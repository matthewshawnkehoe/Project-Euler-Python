'''
Project Euler : Problem 33
@author: Matthew Kehoe
'''
from fractions import Fraction
import time

start = time.time()

# Iterate over all numbers from 10 to 99 in the numerator and denominator
product_num = 1
product_den = 1
for num in range(10, 100):
    for den in range(10, 100):
        # Return the numerator / denominator
        reduced = num / den
        # If numerator / denominator >= 1.0, continue
        if reduced >= 1.0:
            continue
        # Set reduced equal to the fractional value of num / den
        reduced = Fraction(num, den)
        # Convert the numerator and denominator to strings to reduce the common number
        numstr = str(num)
        denstr = str(den)
        for n in numstr:
            # The same number of 0 in the numerator and denominator is the trivial case
            if n == '0':
                continue
            # If the same number is in the numerator and denominator, remove it
            if n in denstr:
                reduced_numstr = numstr.replace(n, '')
                reduced_denstr = denstr.replace(n, '')
                # Check to make sure that we don't divide by zero or have no string length
                if len(reduced_numstr) == 0 or len(reduced_denstr) == 0 or int(reduced_denstr) == 0:
                    continue
                # Convert the reduced numerator and denominator to a fraction
                string_reduced = Fraction(int(reduced_numstr), int(reduced_denstr))
                # Check if the reduced string is the same as the original reduced float
                if string_reduced == reduced:
                    print(reduced_numstr + '/' + reduced_denstr + '==' + str(num) + '/' + str(den))
                    # Multiply both numerator and denominator products by the reduced values
                    product_num *= int(reduced_numstr)
                    product_den *= int(reduced_denstr)

print(product_num)
print(product_den)
product = Fraction(product_num, product_den)
val = product

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))

