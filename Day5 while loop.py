Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #while loop
>>> st  = 'python is best programming language'
>>> for i in range(len(st)):
	end_value = '-'
	if st[i]==' ' or i== len(st)-1 or st[i+1] == ' ':
		end_value = ' '
	if i%2 == 0:
		print(st[i].upper(), end=end_value)
		else:
			
SyntaxError: invalid syntax
>>> #while loop
>>> st  = 'python is best programming language'
>>> for i in range(len(st)):
	end_value = '-'
	if st[i]==' ' or i== len(st)-1 or st[i+1] == ' ':
		end_value = ' '
	if i%2 == 0:
		print(st[i].upper(), end=end_value)
	else:
		print(st[i].lower(), end=end_value)
	print()

	
P-
y-
T-
h-
O-
n 
  
i-
S 
  
B-
e-
S-
t 
  
p-
R-
o-
G-
r-
A-
m-
M-
i-
N-
g 
  
l-
A-
n-
G-
u-
A-
g-
E 
>>> # integer input till presses q
>>> while True:
	num = input()
	if num == 'q':
		break

	






