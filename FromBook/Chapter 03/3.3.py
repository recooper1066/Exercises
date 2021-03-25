# Exercise 3.3
# author: Bob Cooper
# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0.
#  If the score is out of range, print an error message. If the score is
#  between 0.0 and 1.0, print a grade using the following table:

try:
    grade = float(input("Enter Grade (0.0 - 1.0):"))
    if grade < 0.0 or grade > 1.0:
        print("Error, number is out of range. ")
    elif grade >= 0.9 and grade <= 1.0:
        print('A')
    elif grade >= 0.8 and grade < 0.9:
        print('B')
    elif grade >= 0.7 and grade < 0.8:
        print('C')
    elif grade >= 0.6 and grade < 0.7:
        print('D')
    else:
        grade >= 0.0 and grade < 0.6
        print('F')
except:
    print("Bad score.")
