#Script to print reverse right triangle
no=int(input("HOW many rows you want to print ?  "))
a=2*no-2
for i in range(0, no):
    for j in range(0, a):
        print(end=" ")
    a = a - 2
    for j in range(0, i+1):
        print("* ",end="")
    print("\r")
 
