# Exercise 3.1
# author: Bob Cooper
# Exercise 1: Rewrite your pay computation to give the employee
# 1.5 times the hourly rate for hours worked above 40 hours.

hours = float(input("Enter Hours:"))
bucksPerHour = float(input("Enter Rate:"))

# Hours greater than 40 get OT
if hours > 40:
    regPay = 40 * bucksPerHour
    # time and a half = 1.5
    otPay = (hours - 40) * (bucksPerHour * 1.5)
    print('  Regular   $', regPay)
    print('+ Overtime  $', otPay)
    print('              -------')
    print('  Total Pay $', regPay + otPay)
    print('\n')

    # referenced
    # https://pythonguides.com/python-print-2-decimal-places/
    print('  Regular   $', "{:.2f}".format(regPay))
    print('+ Overtime  $', "{:.2f}".format(otPay))
    print('              -------')
    print('  Total Pay $',  "{:.2f}".format(regPay + otPay))
else:
    print('  Total Pay $',  "{:.2f}".format(hours * bucksPerHour))
