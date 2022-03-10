a=int(input('Enter any number : '))
no=a
re=sum=0
while(a>0):
	re=a%10
	a=a//10
	sum=sum+re**3
print('armstrong number' if sum==no else 'not armstrong number')