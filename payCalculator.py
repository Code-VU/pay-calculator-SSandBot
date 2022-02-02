# from platform import python_branch
def calculatePay():
# Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    hrs = input("Enter Hours: ")
    float(hrs)
    rate = input("Enter Rate: ")
    float(rate)
    if input (hrs) <= 40: 
        regpay = float(hrs) * float(rate)
        pay = regpay
    elif float(hrs) > 40:
        pay = (float(hrs)*rate) + (float(hrs)-40*(rate)*1.5)  
    print ("Pay: ", pay)
       # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay ()