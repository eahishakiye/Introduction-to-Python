# A function condition()
def condition():
    """A function with if statement. From line 4 to line 7, it is refered to as function definition"""
    """A function is defined not created"""
    """Calling a function is called to invoke a function"""
    number = 10
    if number > 0:
        print("Number is positive")
    print("if statement is easy")
condition()

# The code below works like the function above
# It is extracted from the function above
number = 10
if number > 0:
    print("Number is positive")
    

def mycondition():
    """The function includes both if and else statements"""
    number = -10
    if number > 0:
        print("Number is positive")
    else:
        print("Number is negative")
    print("This statement has nothing to do with the if conditions above")

mycondition()