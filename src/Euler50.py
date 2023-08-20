'''
Project Euler : Problem 50
@author: Matthew Kehoe
'''
import time

start = time.time()


def primes(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

# Prime numbers up to one million
N = 1000000
primes = primes(N)

# Length of the prime list
length_prime_list = len(primes)

# length of maximum consecutive prime sum
length = 0

val = 0
for i in range(length_prime_list):
  # Start from i + length to account for the largest length of consecutive prime sum found.
  for j in range(i + length, length_prime_list):
    current_length = len(primes[i:j])
    total = sum(primes[i:j])
    if total < N:
      if total in primes and current_length > length:
        length = current_length
        val = total
    else:
      break

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))



