camels = 42
print('%d' % camels)

print('I have spotted %d camels.' % camels)

# Formatting Types
# %d - integers
# %g -
print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))


# Code: http://www.py4e.com/code3/copytildone2.py
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
    print(line.upper())
    print(line.capitalize())
print('Done!')

print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))
