# Emmanuel Ahishakiye
# The following is the summary of what we covered
# we started by introduction, creating variables 
# and printing values of the variables
# example
num1 = 12
print(f"The value of num1 is {num1}")

# the following snippet of code creates sting variables
fname = "Ahishakiye"
lname = "Emmanuel"
fullName = f"{fname} {lname}"
print("My name is", fullName)

# we also discussed about lists
list1 = [1,3,5,7,9,10,13]
for item in list1:
    print(item)

#item1 = 2
for item1 in range(1,20):#Range helps to display a list of items from the start to the end 
    print(item1)

myrange = input("Please enter your range: ")
for num in range(1, int(myrange)):
    if num > 10:
        print("Out of range")
    else:
        print("Inside the range")
        
        
# we also discussed about arithmetic operators in python
#Addition
a = 13
b = 4
c = a + b
print(c)

#Subtraction
c = a - b
print(c)

#Multiplication
c = a * b
print(c)

#Division
c = a / b
print(c)

#Integer Division or floor division
c = a // b
print(c)

#Exponent
c = a ** b
print(c)

#Modulus. This gives a remainder 
c = a % b
print(c)


# we also discussed about functions

def myfunction():
    num1, num2 = 20, 40
    print(num1 + num2)
# function call    
myfunction()

def multidata1(animal_type, pet_name):
    """The function will display information about a pet"""
    print(f"\n I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
    
multidata1("hamster", "james")


# we then discussed code packaging, where we discussed the following
# Python is extremely moduler and is object oriented
# A module is a piece code that does some function (to achieve some functionality)
# Modules help to create packages which perform some activity
# we want to prepare and structure our code so that it can be reused
# Start calling a folder but a directory
# A file in python is called a script
# A folder (directory) that contains a script(s), and if the script is used as a python function, the package becomes a package and the #script is a module

# Python is extremely moduler and is object oriented
# A module is a piece code that does some function (to achieve some functionality)
# Modules help to create packages which perform some activity
# we want to prepare and structure our code so that it can be reused
# Start calling a folder but a directory
# A file in python is called a script
# A folder (directory) that contains a script(s), and if the script is used as a python function, the package becomes a package and the #script is a module
# OOP is a paradigm of software development based on real world objects
# Classes vs objects
# OOP principles
# 1. Polymorphism
# 2. Inheritance
# 3. Abstraction
# 4. Encapsulation
# A class is a blueprint of an object
# A blue print is an original copy of something e.g. Emma is a blue print of a man.
# An individual created from the blueprint is an object
# An Object is an instance of a class
# These objects have things in common from the master print (the class)
# Ahishakiye (object)is an instance of a person (class)
# A class gives an existence of object
# we create variables of class (properties) and we give full meaning to have an object

# Attributes of animal
# Should have name, legs, color. Any animal should have those properties
# if you want to understand a class of an object we use "is a"
# A cat is an object and animal is a class

# Abstraction, you hide some details that may not be necessary
# E.g museveni is a dad, and therefore while at home we handles family business as a father and husband.
# some information is private like age, number of body counts 

# inheritance. You have a concept of a parent and child
# Toyota is a child of a car
# Techno is a child of a smart phone
# Inheritance is the ability by an object to take on attributes from different classes
# Eg Toyota wish belongs to toyota class and Car class

# Polymorphism is the ability to take different forms
# Eg Museveni is a pres1dent, a father, a soldier, a grand father

# Encapsulation
# Ability to have what to share and what not to share
# Public, protected and private

# Defining an object in Class
# we use the keyword Class, the name of the class starts with capital letter
class Animal:
    color = ""
    size = ""
    sex = ""
    name = ""
    sound = ""
    species = ""  
    age = 0 

# A function defined with in a class is called the method and the statements within the class is the behavious
    def feed(self): # the method
        """A method of the function"""
        return "Animal feeds by chewing" # The behaviour
        #return 0
        
      
# Creating objects of the class animal
#The feautes of the class are identified by the dot operator or access specifier
cat = Animal()
cat.color = "black"
cat.size = "medium"
cat.sex = "male"
cat.name = "Tom"
cat.sound = "meow"
cat.species = "lion"
cat.age = 20

# Accessing objects
print(f"{cat.name} is {cat.age} years old")
print(cat.name + " does " + cat.sex)

# creating other objects of the class Animal()
dog = Animal()
dog.color = "black"
dog.size = "big"
dog.sex = "male"
dog.name = "Dick"
dog.sound = "WuWu"
dog.species = "Cat"
dog.age = 10

# creating other objects of the class Animal()
cow = Animal()
cow.color = "black"
cow.size = "big"
cow.sex = "male"
cow.name = "Bihogo"
cow.sound = "WuWu"
cow.species = "Cattle"
cow.age = 5

#END