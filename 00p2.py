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
#The features of the class are identified by the dot operator or access specifier
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

print(f"{cow.name} is {cow.sex}")

# creating other objects of the class Animal()
lion = Animal()
lion.color = "black"
lion.size = "big"
lion.sex = "male"
lion.name = "Dick"
lion.sound = "WuWu"
lion.species = "Cat"
lion.age = 10

# A thing that an animal makes to its self and to others is a method, and how it does it is a behaviour 
print(lion.feed())