# Exercise 3:
def count(str, chr):
    cnt = 0
    for letter in str:
        if letter == chr:
            cnt = cnt + 1
    return cnt

# Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the
# string and the letter as arguments.


fruit = "Banana"
print(count(fruit, 'a'))
