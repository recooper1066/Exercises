# Exercise 4: There is a string method called count that is similar to the function in the previous exercise.
# Read the documentation of this method at https://docs.python.org/3.5/library/stdtypes.html#string-
# methods and write an invocation that counts the number of times the letter a occurs in "banana".


def count(str, chr, iStart, iStop):
    cnt = 0
    idx = iStart
    if iStop > len(str) or iStart > len(str):
        cnt = -1
    else:
        while idx < iStop:
            if str[idx] == chr:
                cnt = cnt + 1
            idx = idx + 1
    return cnt
# Encapsulate this code in a
# function named count, and generalize it so that it
# accepts the string and the letter as arguments.


fruit = "Banana"
print(count(fruit, 'a', 1, 1))
print(count(fruit, 'a', 1, 2))
print(count(fruit, 'a', 1, 3))
print(count(fruit, 'a', 1, 4))
print(count(fruit, 'a', 9, 5))
