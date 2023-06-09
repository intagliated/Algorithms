#Program to check if  a number is a palindrome 

number=int(input("Enter the number :"))
str_number =str(number)
rev =str_number[::-1]
if(rev==str_number):
	print("Palindrome")
else :
	print("Not a  Palindrome")
