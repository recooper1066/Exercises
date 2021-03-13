# Exercise 4.6
# author: Bob Cooper

def PayCompute (hours, rate):
    # Hours greater than 40 get OT
    if hours > 40:
        #regPay = 40 * rate
        # time and a half = 1.5
        otPay = (hours - 40) * (rate * 1.5)
        Pay = (40 * rate) + otPay
    else :
        Pay = hours * rate
    return Pay


hours = float( input ("Enter Hours:"))
rate = float( input ("Enter Rate:"))
print ("Pay: ", PayCompute(hours, rate) )
