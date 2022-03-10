#Script to print simple right angle triangle. 
no=int(input("How many time you want to print the pyramid ? "))
for i in range(0,no):
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")
