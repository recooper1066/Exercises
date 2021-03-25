# Exercise 4.6
# author: Bob Cooper
# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).

def ComputePay(hours, rate):
    try:
        # Hours greater than 40 get OT
        if hours > 40:
            regPay = 40 * rate
            # time and a half = 1.5
            otPay = (hours - 40) * (rate * 1.5)

            # http://cis.bentley.edu/sandbox/wp-content/uploads/Documentation-on-f-strings.pdf
            print('  Regular   $', "{:7.2f}".format(regPay))
            print('+ Overtime  $', "{:7.2f}".format(otPay))
            print('              -------')
            print('  Total Pay $',  "{:7.2f}".format(regPay + otPay))
        else:
            print('  Total Pay $',  "{:7.2f}".format(hours * rate))
    except:
        print('Could not Calculate Pay.  Please retry and check values input.')
        quit()


try:
    hours = float(input("Enter Hours:"))
    #hours = input ("Enter Hours:")
    bucksPerHour = float(input("Enter Rate:"))
except:
    print("Error, please enter numeric input. ")
    quit()

ComputePay(hours, bucksPerHour)
