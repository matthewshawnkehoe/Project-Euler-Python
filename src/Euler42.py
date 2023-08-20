'''
Project Euler : Problem 42
@author: Matthew Kehoe
'''
import functools
import time
start = time.time()

# Open the words.txt file and read the content
f = open('words.txt', 'r')  # open words.txt in read mode
d = f.read()
f.close()

# Replace the double quotes with nothing and then sort alphabetically
d = d.replace('"', '')
words = d.split(',')
words.sort()

# Find the letter score for every char. A = 1 and Z = 26.
@functools.lru_cache(maxsize=None)
def letter_score(char):
    ord_a = ord('A')
    return ord(char) - ord_a + 1

# Calculate all triangle numbers.
def triangleNumber(n):
    if n == 1:
        return 1
    for i in range(1, n):
        return int(0.5 * n * (n+1))

# Calculate the sum of all word values in a word.
# Example: SKY is worth 19 + 11 + 25 = 55 = t_10
def word_worth(word):
    return sum(letter_score(l) for l in word)

# Make a list of triangle numbers
triangle = [triangleNumber(i) for i in range(1, len(words))]

# Iterate over the list of words and increase the counter by one if
# the word is a triangle word
count = 0
for word in words:
    worth = word_worth(word)
    if worth in triangle:
        count += 1

val = count

elapsed = (time.time() - start)

print("%s found in %s seconds" % (val, elapsed))
