# Exercise 4.1
# author: Bob Cooper
# Exercise 7: Rewrite the grade program from the
# previous chapter using a function called computegrade that
#  takes a score as its parameter and returns a grade as a string.

def computergrade(score):
    if grade >= 0.9 and grade <= 1.0:
        print('A')
    elif grade >= 0.8 and grade < 0.9:
        print('B')
    elif grade >= 0.7 and grade < 0.8:
        print('C')
    elif grade >= 0.6 and grade < 0.7:
        print('D')
    else:
        print('F')


try:
    grade = float(input("Enter Grade (0.0 - 1.0):"))
    if grade < 0.0 or grade > 1.0:
        print("Error, number is out of range.")
    computergrade(grade)
except:
    print("Bad score.")
