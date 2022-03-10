a=int(input('Enter any number'))
no=a
sum=0
while(a>0):
	sum=sum+a%10
	a=a/10
print("The sum of diguts of {} is {}.".format(no,sum))
	