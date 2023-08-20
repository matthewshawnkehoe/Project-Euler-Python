'''
Project Euler : Problem 51
@author: Matthew Kehoe
'''

import functools
import time


start = time.time()


@functools.lru_cache(maxsize=None)
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6
    return True


def prime_sieve(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]


# Check if the prime number generates eight other primes after replacing three repeated digits
# Replace the repeated digit with all others digits 0,1,2,3,4,5,6,7,8,9 and check if
# eight of the new numbers are prime
def eight_prime_family(prime, rep_digit):
    number_of_primes_in_fam = 0
    for digit in '0123456789':
        n = int(str.replace(prime, rep_digit, digit))
        if (n > 100000 and is_prime(n)):
            number_of_primes_in_fam += 1
    return number_of_primes_in_fam == 8


# Only check 6 digit prime numbers with 3 repeating digits
for prime in prime_sieve(1000000):
    if (prime > 100000):
        s = str(prime)
        # for an eight prime value family, only check primes that have their repeating digit 0, 1, or 2
        if (s.count('0') == 3 and eight_prime_family(s, '0') \
                or s.count('1') == 3 and eight_prime_family(s, '1') \
                or s.count('2') == 3 and eight_prime_family(s, '2')):
            val = s

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))