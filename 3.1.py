# Exercise 3.1
# author: Bob Cooper
hours = float( input ("Enter Hours:"))
#hours = input ("Enter Hours:")
bucksPerHour = float( input ("Enter Rate:"))

# Hours greater than 40 get OT
if hours > 40:
    regPay = 40 * bucksPerHour
    # time and a half = 1.5
    otPay = (hours - 40) * (bucksPerHour * 1.5)
    print ('  Regular   $', regPay )
    print ('+ Overtime  $', otPay)
    print ('              -------')
    print ('  Total Pay $', regPay + otPay)
else :
    print ('  Total Pay $', hours * bucksPerHour)