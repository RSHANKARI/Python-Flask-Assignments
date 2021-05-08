Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Number divisible by 5 and 7 both
>>> uplim = 1000
>>> lowlim = 2
>>> for i in range(lowlim,uplim):
	if i%7 == 0 and i%5 == 0:
		print(i,end = " ", sep = ",")

		
35 70 105 140 175 210 245 280 315 350 385 420 455 490 525 560 595 630 665 700 735 770 805 840 875 910 945 980 
>>> 
>>> #Sum of series
>>> n = int(input("Enter a number n: "))
Enter a number n: 2
>>> temp=str(n)
>>> t1=temp+temp
>>> t2=temp+temp+temp
>>> t3=temp+temp+temp+temp
>>> t4=temp+temp+temp+temp+temp
>>> comp=n+int(t1)+int(t2)+int(t3)+int(t4)
>>> print("The value is:",comp)
The value is: 24690
>>> 
>>> #factorial using while loop
>>> n = int(input("Enter a number:"))
Enter a number:5
>>> fact = 1
>>> while(n >= 2):
	fact =fact*n
	n-=1

	
>>> print("factorial:" , fact)
factorial: 120
>>> 