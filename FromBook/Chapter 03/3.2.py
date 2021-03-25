# Exercise 3.2
# author: Bob Cooper
# Exercise 2: Rewrite your pay program using try and except so
# that your program handles non-numeric input gracefully by printing
# a message and exiting the program.

try:
    hours = float(input("Enter Hours:"))
    #hours = input ("Enter Hours:")
    bucksPerHour = float(input("Enter Rate:"))
except:
    print("Error, please enter numeric input. ")
    quit()

try:
    # Hours greater than 40 get OT
    if hours > 40:
        regPay = 40 * bucksPerHour
        # time and a half = 1.5
        otPay = (hours - 40) * (bucksPerHour * 1.5)
        # referenced
        # http://cis.bentley.edu/sandbox/wp-content/uploads/Documentation-on-f-strings.pdf
        print('  Regular   $', "{:7.2f}".format(regPay))
        print('+ Overtime  $', "{:7.2f}".format(otPay))
        print('              -------')
        print('  Total Pay $',  "{:7.2f}".format(regPay + otPay))
    else:
        print('  Total Pay $',  "{:7.2f}".format(hours * bucksPerHour))
except:
    print('Could not Calculate Pay.  Please retry and check values input.')
