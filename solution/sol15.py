rows=int(input("Enter rows number : "))
no=1
for a in range(1,rows+1):
    for b in range(1,a+1):
        print(no,end=' ')
        no=no+1
    print()
