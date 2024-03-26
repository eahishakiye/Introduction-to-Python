# think of a class as a set of instructions for how to make an instance
# the first parameter in the shish method (self) is used for identifying the properties of a method
class Lake:
    """we are creating a class Lake"""
    # This is shishi method. it is a special method used in python to identify properties of a class
    # It is a rule, the fisrt parameter of the shish method to start with self. because it refers to an individual object
    # self is a pointer to the properties of the class. that is why each property of the method starts with self, eg self.name
    def __init__(self, name, location, size, depth): 
        """we are defining the attributes of the class"""
        self.name = name
        self.location = location
        self.size = size
        self.depth = depth

class River:
    def __init__(ozzy, name, location, length):
        ozzy.name = name
        ozzy.location = location
        ozzy.length = length
    # we can use another word not necessarily self, but for uniformity, we use self. All methods in a class must have the word self.
    
# The Automobile class holds general data
# about an automobile in inventory.
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

# creating objects of the class Lake
lake1 = Lake("victoria", "Kampala", 100, 10)