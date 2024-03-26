# Assignment5 - Emmanuel Ahishakiye

# The first function that prompts a user to input name, age, email, gender and it prints them out
def personal_details(fname, lname, age1, email, gender):
    full_name = f"{fname} {lname}"
    print("Your Name is :", full_name.title())
    print("Your Age is :", age1)
    print("Your Email is :", email)
    print("Your Gender is :", gender.title())

# Getting user inputs:
fname = input("Please Enter Your First Name: ")
lname = input("Please Enter Your Last Name: ")
age = input("Please Enter Your Age: ")
email = input("Please Enter Your Email: ")
gender = input("Please Enter Your Gender: ")
# Calling the function
personal_details(fname, lname, age, email, gender)

# A function that prompts a user to input paye (30%), nssf(5%), gross pay and then it calculates net pay
# I have tried to implement exception handling
def net_pay(gross, paye, nssf):
    """"A function for calculating net salary from gross salary"""
    try:
        paye = (paye/100) * gross # Pay As You Earn tax rate
        nssf = (nssf/100) * gross # NSSF contribution rate
        net = gross - (paye + nssf)
    
    except ValueError:
        print("Please enter valid Figures.")
    
    except Exception as e:
        print("An error occurred:", e)
    else:
        print("The Net Pay is:", net)
    
# Getting user inputs:
gross = float(input("Please Enter your Gross Pay: "))
paye = int(input("Please Enter the PAYE: "))
nssf = int(input("Please Enter the NSSF: "))
# Calling the function
net_pay(gross, paye, nssf)

