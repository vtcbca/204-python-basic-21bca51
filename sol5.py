no1=int(input('Enter any number : '))
no2=1
while(no2<10):
    if(no1%no2==0):
        print("{} is divisible by {}".format(no1,no2))
    no2=no2+1
