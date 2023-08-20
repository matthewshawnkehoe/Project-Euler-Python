'''
Project Euler : Problem 22
@author: Matthew Kehoe
'''
import functools
import time
start = time.time()

# Open the names.txt file and read the content
f = open('names.txt', 'r')  # open names.txt in read mode
d = f.read()
f.close()

# Replace the double quotes with nothing and then sort alphabetically
d = d.replace('"', '')
names = d.split(',')
names.sort()

# Find the letter score for every char. A = 1 and Z = 26.
@functools.lru_cache(maxsize=None)
def letter_score(char):
    ord_a = ord('A')
    return ord(char) - ord_a + 1

# Calculate the sum of all letter scores in a name.
# Example: COLIN is worth 3 + 15 + 12 + 9 + 14 = 53
def name_worth(name):
    return sum(letter_score(l) for l in name)

# Return the name score which is name_score = name_worth(name) * index_in_names_list
# The index starts at 0, so add 1
def name_score(name, index):
    return name_worth(name) * (index + 1)

# print (name_worth("COLIN")) # Should return 53
# Sum the name score for every name inside names
val = sum(name_score(names[i], i) for i in range(len(names)))

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))
