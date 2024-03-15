# The statement creates a string variable called some_string and then assigning it a string called "python is fun"
some_string = 'Python is fun' 
#The below statement creates three variables a, b, c and assigned them values 5, 3.2 and 'Hello' respectively
a, b, c = 5, 3.2, 'Hello'

print(a)  # This statement will print the value of the variable a which is 5.
print(b)  # This statement will print the value of the variable b which is 3.2.
print(c)  # This statement will print the value of the variable c which is 'Hello'.

# The statement below creates a variable called num1 and then assignes it an integer value of 5.
num1 = 5
# The statement will print the datatype of the variable num1 which is integer.
print(num1, 'is of type', type(num1))
# The statement below creates a variable called num2 and then assignes it a float value of 2.0.
num2 = 2.0
# The statement will print the datatype of the variable num2 which is float.
print(num2, 'is of type', type(num2))
# The statement below creates a variable called num3 and then assignes it a complex value of 1+2j.
num3 = 1+2j
# The statement will print the datatype of the variable num3 which is complex type.
print(num3, 'is of type', type(num3))
# The statement below creates a list called languages
languages = ["Swift", "Java", "Python"]

# The statement prints the first item in the languages list which is 'Swift'.
print(languages[0])   # 

# The statement prints the third item in the languages list which is 'Python'.
print(languages[2])   # 

#  The statement creates a turple called product
product = ('Microsoft', 'Xbox', 499.99)

# The statement prints the first item in the turple which is 'Microsoft'
print(product[0])   # Microsoft

# The statement prints the second item in the turple which is 'Xbox'
print(product[1])   # Xbox


# The statement creates a dictionary called capital_city
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
# The statement prints the keys and their values of the dictionary
print(capital_city)


# The statement creates a set called student_id
student_id = {112, 114, 116, 118, 115}

# The statement prints the values of the set called student_id
print(student_id)

# The statement prints a set as the datatype of the variable student_id 
print(type(student_id))

# The statement creates a list called fruits
fruits = ["apple", "mango", "orange"] 
# The statement prints the values of of the list fruits
print(fruits)

# The statement creates a turple called numbers
numbers = (1, 2, 3) 
# The statement prints the values of the turple called numbers
print(numbers)

# The statement creates a dictionary called alphabets
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
# The statement prints the keys and their values for the dictionary called alphabets
print(alphabets)

# The first statement below creates a set called vowels 
# then the second statement prints the values or the elements of the set called vowels
vowels = {'a', 'e', 'i' , 'o', 'u'} 
print(vowels) 


# The statement creates a set called student_id
student_id = {112, 114, 116, 118, 115}

# The statement prints the elements or the values of the set called student_id
print(student_id)

# The statement prints a set as the datatype of the variable student_id
print(type(student_id))

# The statement creates a turple called product
product = ('Microsoft', 'Xbox', 499.99)

# The statement prints the first item in the turple which is 'Microsoft'
print(product[0])   # 

# The statement prints the second item in the turple which is 'Xbox'
print(product[1])   # Xbox


# The first statement creates a variable called a and assignes it a value of 7 and 
# the second statement creates b variable called a and assignes it b value of 2
a = 7
b = 2

# The statement prints the sum of a and b which is 9
print ('Sum: ', a + b)  

# The statement prints the difference of a and b (subtracts b from a) which is 5.
print ('Subtraction: ', a - b)   

# The statement prints the product of a and b which is 14
print ('Multiplication: ', a * b)  

# The statement prints the result of the division of a by b
print ('Division: ', a / b) 

# The statement prints the product of the floor division a by b which is 3
print ('Floor Division: ', a // b)

# The statement prints the remainder of the division of a by b which is 1
print ('Modulo: ', a % b)  

# The statement prints the value of a to the power of b which is 49
print ('Power: ', a ** b)   


# The statement creates a variable called a and assigned it a value of 10
a = 10

# The statement creates a variable called b and assigned it a value of 5
b = 5 

# The statement adds b to a
a += b      # This is similar to a = a + b
print(a)
# Output: 15
 


# The statement compares a and b prints a==b=false because a is not equal to b
print('a == b =', a == b)

# The statement compares a and b prints a != b=True because a is not equal to b
print('a != b =', a != b)

# The statement compares a and b prints a > b=True because a is greater than to b
print('a > b =', a > b)

# The statement compares a and b prints a < b=False because a is not less than to b
print('a < b =', a < b)

# The statement compares a and b prints a >= b=True because a is greater than to b
print('a >= b =', a >= b)

# The statement compares a and b prints a <= b=False because a is not less or equal to b
print('a <= b =', a <= b)
# The statement prints False because both conditions are not true.
print((a > 2) and (b >= 6)) 

# Logical True and False
print(True and True)     # The statement will print True because logical True and True evaluates to True
print(True and False)    # The statement will print False because logical True and False evaluates to False

# logical True OR False
print(True or False)     # The statement will print True because logical True or False evaluates to True

# Negation
print(not True)          # This statement evaluates to False because the opposite of not True is False

# Creating variables and assigning them values 
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
# The statement logically evaluates whether x1 is equal to y1
print(x1 is not y1)  # The statement will print false 
# The statement logically evaluates whether x2 is equal to y2
print(x2 is y2)  # The statement will print True 
# The statement logically evaluates whether x3 is equal to y3
print(x3 is y3)  # The statement will print false
# The statement creates a variable called message and assigns it a value "Hello world"
message = 'Hello world'
# The statement creates a dictionary called dict1
dict1 = {1:'a', 2:'b'}
# The statement checks whether letter H is contained in the message
print('H' in message)  # prints true

# The statement checks whether the string hello is contained in the value of the variable message
print('hello' not in message)  # prints True because python is case sensitive and the string hello is not in message

# The statement checks whether 1 is a key in the dictionary dict1
print(1 in dict1)  # prints True because 1 is the key in the dictionary dict1

# The statement checks whether 'a' is a key in the dictionary dict1
print('a' in dict1)  # prints false 


















