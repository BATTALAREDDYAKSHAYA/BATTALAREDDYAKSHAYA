#write a program to divide real numbers
a=input("Enter a number:")
b=input("Enter the number:")
if(type(a)=='int' or 'float')and(type(b)=='int' or 'float'):
	div=a/b
	print("the division is",div)
else:
	print("The given number is not real number")
	
