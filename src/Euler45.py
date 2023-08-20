'''
Project Euler : Problem 45
@author: Matthew Kehoe
'''
import time
start = time.time()


# Calculate the triangle number
def triangleNumber(n):
    return n*(n+1)//2

# Calculate the pentagon number
def pentagonNumber(n):
    return n*(3*n-1)//2

# Calculate the hexagon number
def hexagonNumber(n):
    return n*(2*n-1)


triangles = set(triangleNumber(n) for n in range(1, 70000))
pentagons = set(pentagonNumber(n) for n in range(1, 70000))
hexagons = set(hexagonNumber(n) for n in range(1, 70000))

triangleNum = 0
for t in triangles:
    if t in pentagons and t in hexagons:
        triangleNum = t

val = triangleNum

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))