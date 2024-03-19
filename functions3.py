def add():
    """An example of a static function"""
    num1, num2 = 10, 20
    sum  = num1 + num2
    print (f'The sum is {sum}')
add()

#Creating a dynamic function

def add1(num1, num2):
    """An example of a dynamic function"""
    sum = num1 + num2
    print(f'The sum is {sum}')
    
add1(2,5)
add1(100,200)
add1(-10,20)

# create programs for subtraction, multiplication, division and pow
def sub1(num1, num2):
    """An example of a dynamic function for subtraction"""
    diff = num1 - num2
    print(f'The difference is {diff}')
    
sub1(2,5)

def multiply1(num1, num2):
    """An example of a dynamic function for multiplication"""
    product = num1 * num2
    print(f'The product is {product}')
    
multiply1(2,5)

def division1(num1, num2):
    """An example of a dynamic function for division"""
    div = num1 / num2
    print(f'The division is {div}')
    
division1(5,5)

def exponent1(num1, num2):
    """An example of a dynamic function for power/exponent"""
    expo1 = num1 ** num2
    print(f'The exponent is {expo1}')
    
exponent1(2,5)

def modulus1(num1, num2):
    """An example of a dynamic function"""
    mod1 = num1 % num2
    print(f'The modulus is {mod1}')
    
modulus1(2,5)

def multidata(num1, num2, name, flt):
    """The function allows multiple data"""
    print(num1)
    print(num2)
    print(name)
    print(flt)
    
multidata(1,2,"Emma",3.4)

def multidata1(animal_type, pet_name):
    """The function will display information about a pet"""
    print(f"\n I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
    
multidata1("hamster", "james")

def countries(name, location, gdp):
    """Prints countries, their location and their gdp"""
    print(name)
    print(location)
    print(gdp)
    
countries("Uganda", "East Africa", "14B")
