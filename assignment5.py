# Write two dynamic functions. The first function that prompts a user to input name, age, email, gender and it prints them out
# Second function should prompt the user to input paye (30%), nssf (11%), gross and then it calculates net pay
# deadline is sunday 9am

def net_pay(gross, paye, nssf):
    """"A function for calculating net salary from gross salary""" 
    paye = 0.3 * gross
    nssf = 0.15 * gross
    net_salary = gross - (paye + nssf)
    return net_salary
def main():
    try:
        x = int(input("Gross Pay: "))
        y = int(input("Enter the PAYE: "))
        z = int(input("Enter the NSSF: "))
        
        result = net_pay(x, y, z)
        print("The Net Pay is:", result)
        
    except ValueError:
        print("Please enter valid figures.")
    
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()