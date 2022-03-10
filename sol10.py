a=int(input('Enter any number : '))
no=a
re=sum=0
while(a>0):
	d=a%10
	re=re*10+d
	a=a//10
print('palindrome number' if re==no else 'not palindrome number')