# from platform import python_branch
def calculatePay () :
# Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    hrs = input("Enter Hours:")
    h = float(hrs)
    xx = input("Enter Rate:")
    x = float(xx)
    if h <= 40: 
        print( h * x)
    elif h > 40:
        print(40*x + (h-40)*1.5*x)         
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay ()