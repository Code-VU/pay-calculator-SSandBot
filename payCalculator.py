# from platform import python_branch
def calculatePay ():
# Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    hrs = input("Enter Hours: ")
    float(hrs)
    rts = input("Enter Rate: ")
    float(rts)
    h=float(hrs)
    if h<=40: 
        pay = h*float(rts)
           
    print ("Pay: ",pay)
# end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay ()