# Assignment - Ahishakiye Emmanuel
# The name of the file is assignment2.py
# In the code below, three functions are created.

# in the first function, a net salary is created, given a gross salary
def salary(gross):
    """"A function for calculating net salary from gross salary""" 
    paye = 0.3 * gross
    nssf = 0.05 * gross
    net_pay = gross - (paye + nssf)
    return net_pay


# In the following function, a net balance on the account is calculated given stated expenses
def expenses(fees):
    """Net balance after fees payment"""
    rent = 600000
    water = 100000
    electricity = 100000
    phone = 20000
    internet = 100000
    fuel = 500000
    food = 300000
    net_balance = salary(6000000) - (fees + rent + water +
                                     electricity + phone + internet + fuel + food)
    return net_balance


# in the following function, the balance at the end of the month after expenses is calculated
def actual_balance():
    tithe = 0.1 * expenses(1500000)
    party = 300000
    balance = expenses(1500000) - (tithe + party)
    print(balance)


actual_balance()
