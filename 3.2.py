# Exercise 3.2
# author: Bob Cooper
try:
    hours = float( input ("Enter Hours:"))
    #hours = input ("Enter Hours:")
    bucksPerHour = float( input ("Enter Rate:"))
except:
    print ("There is a problem with inputed values. ")
    quit()

try:
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
except:
    print ('Could not Calculate Pay.  Please retry and check values input.')    