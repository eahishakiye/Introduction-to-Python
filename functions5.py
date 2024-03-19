#How can we make functions communicate with one another

def vat(rate, price):
    """Calculate the value added tax on a given amount."""
    frate  = (rate/100)*price
    return frate 
# We have to use return keyword to have functions to share information
# Return is the last statement that marks the end of the function
    #print(int(frate))
#vat(18,20000)

def netprice():
    actual_price = vat(18,20000)
    net_price = int(actual_price + 20000)
    print(net_price)
    
netprice()

#Assignment # Paste the code into the body of the email, and the deadline is today at 9pm

# Create atleast three functions that share their variables and print the last function
# The two of them should be parameterised. The first function should return to the second 
# and the second return to the third, and the third should print the results