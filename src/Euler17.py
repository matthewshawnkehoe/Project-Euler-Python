'''
Project Euler : Problem 17
@author: Matthew Kehoe
'''
import time
start = time.time()

def convert_num_2_words(num):
    units = ("", "one ", "two ", "three ", "four ","five ", "six ", "seven ","eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ", "seventeen ", "eighteen ", "nineteen ")
    tens =("", "", "twenty ", "thirty ", "forty ", "fifty ","sixty ","seventy ","eighty ","ninety ")

    if num < 0:
        return "minus "+convert_num_2_words(-num)

    if num < 20:
        return  units[num]

    if num < 100:
        return  tens[num // 10]  +units[int(num % 10)]

    if num % 100 == 0 and num < 1000:
        return units[num // 100]  +"hundred " +convert_num_2_words(int(num % 100))

    if num < 1000:
        return units[num // 100]  +"hundred and " +convert_num_2_words(int(num % 100))

    if num % 1000 == 0 and num < 1000000:
        return  convert_num_2_words(num // 1000) + "thousand " + convert_num_2_words(int(num % 1000))

    if num < 1000000:
        return  convert_num_2_words(num // 1000) + "thousand and " + convert_num_2_words(int(num % 1000))

    if num % 1000000 == 0 and num < 1000000000:
        return convert_num_2_words(num // 1000000) + "million " + convert_num_2_words(int(num % 1000000))

    if num < 1000000000:
        return convert_num_2_words(num // 1000000) + "million and " + convert_num_2_words(int(num % 1000000))

    return convert_num_2_words(num // 1000000000)+ "billion and "+ convert_num_2_words(int(num % 1000000000))

# The isalpha() methods returns “True” if all characters in the string are alphabets, Otherwise, It returns “False”.
def return_num_count(num):
    # Add one to sum only if the char is alpha
    return sum(1 for l in convert_num_2_words(num) if l.isalpha())

val = sum(return_num_count(i) for i in range(1, 1001))

elapsed = (time.time() - start)

print ("%s found in %s seconds" % (val,elapsed))