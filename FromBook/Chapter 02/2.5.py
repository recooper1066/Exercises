# Exercise 2.5
# Bob Cooper
# Exercise 5: Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and
# print out the converted temperature.
tempC = input('°C:')
try:
    fval = float(tempC)
    print('°F:', fval * 1.8 + 32)
except:
    print('Not a number.')
