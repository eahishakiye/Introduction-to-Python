# Emmanuel Ahishakiye
# Assignment7 on Classes, their methods and behaviours
# Define five classes with atleast five parameters and create atleast 3 different objects
class Dog:
    """A dog class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Tom", 12)
print(f"{dog1.name} is {dog1.age} years  old.")

class Automobile:
# The __init__ method accepts arguments for the
# make, model, milieage, and price. It initializes
# the data attributes with these values.
# self connects the parameters with the properties
    def __init__(self, make, model, mileage, price):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.price = price
        
automobile1 = Automobile("Toyota", "Camry", 5000, 500000)
print(f"The car name is {automobile1.make}, model is {automobile1.model}, the mileage is {automobile1.mileage} and its price is {automobile1.price}.")

class Cow:
    """A class cow"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

cow1 = Cow("Bihogo", 20)
print(f"{cow1.name} is {cow1.age} years  old.")

class Apartment:
    """A class apartment"""
    def __init__(self, name, location, size):
        self.name = name
        self.location = location
        self.size = size

apartment1 = Apartment("Emmex", "Gayaza", "12ft")
print(f"The Apartment {apartment1.name} is located in {apartment1.location} and it is  {apartment1.size}")


class Goat:
    """A class cow"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

goat1 = Goat("Cyungo", 20)
print(f"{goat1.name} is {goat1.age} years  old.")
    
    
    
