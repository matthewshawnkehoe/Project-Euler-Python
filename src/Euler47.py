'''
Project Euler : Problem 47
@author: Matthew Kehoe
'''
import time

start = time.time()


def unique_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in factors:
                factors.append(i)
    if n > 1 and n not in factors:
        factors.append(n)
    return factors


# Consecutive Numbers
consecutive = set(i for i in range(2, 500000))


first_num = 0
for i in consecutive:
    len_fact_i = len(unique_prime_factors(i))
    len_fact_i_plus_one = len(unique_prime_factors(i + 1))
    len_fact_i_plus_two = len(unique_prime_factors(i + 2))
    len_fact_i_plus_three = len(unique_prime_factors(i + 3))
    if len_fact_i == 4 and len_fact_i_plus_one == 4 and len_fact_i_plus_two == 4 and \
        len_fact_i_plus_three == 4:
            print(i, i+1, i+2, i+3)
            first_num = i
            break

val = first_num

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))