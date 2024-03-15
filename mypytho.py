#Name: Emmanuel Ahishakiye.
#I started from where we started introduction to python programming

#Printing something. 
print("Welcome to Python Programming!")

#Variables in pthon are used to store values in memory
#In the program below, i am creating variables x and y and then performing the an addition and storing the results in a variable z.
x = 40
y = 12
z = x + y
print(x)
print(y)
print(z)

#working with strings
language = "python"
print(language)
print("Emmanuel is learning Python programming")

# Python Data types
#we have data types namely; numeric (int, float, complex), text type (string), sequence type (list, turple, range), mapping (dict), set, and bool

#Python Numeric Data type
#This is integer type 
num1 = 10
print(num1, " is type of ", type(num1))

#This is float example
num2 = 10.2
print(num2, " is type of ", type(num2))

#This is a complex type
num3 = 10 + 3j
print(num3, " is type of ", type(num3))

#Python String Data Type
name = "Emmanuel Ahishakiye"
print(name)

#Python List Data Type
#simple list
cities = ["Kampala", "Nairobi", "Kigali", "Arusha"]
print(cities)
print(cities[-1])

#Example two
country = ["Uganda", "Kenya", "Tanzania", ["Egypt", "Somalia", ["Sudan", ["Burundi", ["Togo"], ["Benin"]]]]]
print(country[-1])
print(country[-1][-1])
print(country[3][2][1])
print(country[-1][-1][-1])
print(country[-1][-1][-1][-1])
print(country[-1][-1][-1][2])
print(country[-1][-1][-1][2][-1])

#tuple type
#The difference between a list and a turple is that list is mutable while turple is immutable
fruits = ("Mango", "Apple", "Tomato", "Jane")

#Mapping - creating a dictionary
person = {"name": "Ahishakiye", 'age': 24, "Gender":'Male'}
print(person)
print(person["name"])
print(person["Gender"])
print(person.keys())
print(person.values())

#Python Set Data Type
#A set of age of students
age = {22, 20, 33, 29, 25}
print(age)

#Python Operators
#we use python operators to perform operations on variables and values.
# These operators are addition, assignment, subtraction, multiplication, division, integer division

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

#Assignment operators
m = 4
p = m + 3
p += 3
p -= 2
p *= 5
p /= 4
p %= 3
p **= 5


