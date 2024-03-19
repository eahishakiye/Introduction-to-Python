def add(a,b):
    ans = a+b
    print(ans)
    

age =20
#Functions are self containedblock of code
#A function can access both local and global variables
def add1(a,b):
    """a and b are parameters. a dynamic functions is well as called a parameterised function"""
    """"The values of the parameters are called arguments"""
    ans = a + b + age
    print(ans)

add1(10,20)
#print(ans). Ans is out of scope because it was defined inside the function
#Local varialbles vs global variables. 
#local variables are within a function. Global values are outside a function




