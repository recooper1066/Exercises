# Exercise 2: Write another program that prompts for a list of
#  numbers as above and at the end prints out both the
#  maximum and minimum of the numbers instead of the average.

maxi = 0.0
mini = 0.0

while True:
    sval = input('Enter a number:')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
# Put first value into min otherwise mini is always 0
    if mini == 0:
        mini = fval

    if fval < mini:
        mini = fval

    if fval > maxi:
        maxi = fval

print('The max is:', maxi)
print('The min is:', mini)
