for num in range(1,10):
    if num > 10:
        print("Out of range")
    else:
        print("Inside the range")


for num in range(1,10):
    if num > 10:
        print("Out of range")
else:
    print("Inside the range")
    

myrange = input("Please enter your range: ")
for num in range(1, int(myrange)):
    if num > 10:
        print("Out of range")
    else:
        print("Inside the range")
        
mylist = [1,2,3,4,5,6,7,8,9]
for i in mylist:
    print(i)
else:
    print("No items left")