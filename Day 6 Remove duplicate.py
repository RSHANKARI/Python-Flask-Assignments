Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Remove duplicate elements in list
>>> list=[1,2,3,4,6,4,3,2]
>>> result=[]
>>> for i in list:
	if i not in result:
		result.append(i)
		print(result)

		
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 3, 4, 6]
>>> #palindrome
>>> s=input("tell me a word to check palindrome:)
	
SyntaxError: EOL while scanning string literal
>>> s=input("tell me a word to check palindrome:")
tell me a word to check palindrome:2442
>>> n=len(s)
>>> sp=s[n::-1]
>>> if s==sp:
	print("s+ is a palindrome")
	else:
		
SyntaxError: invalid syntax
>>> if s==sp:
	print("s+ is a palindrome")
else;
SyntaxError: invalid syntax
>>> if s==sp:
	print("s+ is a palindrome")
else:
	print("s+ is not a palindrome")

	
s+ is a palindrome
>>> s=input("tell me a word to check palindrome:")
tell me a word to check palindrome:ADDA
>>> n=len(s)
>>> sp=s[n::-1]
>>> if s==sp:
	print(s+ "is a palindrome")
else:
	print("s+ is not a palindrome")

	
ADDAis a palindrome
>>> 