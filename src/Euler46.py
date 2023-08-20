'''
Project Euler : Problem 46
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


primes = primes(10000)
twice_squares = [2*i*i for i in range(10000)]
goldbach = set((primes[i] + twice_squares[j]) for i in range(1000) for j in range(1000))


val = 0
for i in range(3, 10000, 2):
    if i not in goldbach and i not in primes:
        val = i
        break

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))