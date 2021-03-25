# Exercise 1: Write a while loop that starts at the last character in
# the string and works its way backwards to the first character in the
# string, printing each letter on a separate line, except backwards.

StrToTrav = 'separate line, except backwards'
index = len(StrToTrav)-1

while index >= 0:
    char = StrToTrav[index]
    print(char)
    index = index - 1
