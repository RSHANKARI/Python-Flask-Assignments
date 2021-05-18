Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str="hello world happy birthday"
>>> ord=str.split(" ")
>>> #Reverse words in string
>>> str="hello world happy birthday"
>>> word=str.split(" ")
>>> print(word)
['hello', 'world', 'happy', 'birthday']
>>> word=word[-1::-1]
>>> print(word)
['birthday', 'happy', 'world', 'hello']
>>> outputstr=' '.join(word)
>>> print(outputstr)
birthday happy world hello
>>> #vowels
>>> sentence = input("enter the sentence:")
enter the sentence:abed
>>> string = sentence.lower()
>>> print(string)
abed
>>> count=0
>>> list1=["a","e","i","o","u"]
>>> for char in string:
	if char in list1:
		count = count+1
		print("number of vowels in given sentence is")

		
number of vowels in given sentence is
number of vowels in given sentence is
>>> sentence = input("enter the sentence:")
enter the sentence:AbeD sEnTence
>>> string = sentence.lower()
>>> print(string)
abed sentence
>>> count = 0
>>> list1=["a","e","i","o","u"]
>>> for char in string:
	if char in list1:
		count = count+1
		print("number of vowels in given sentence is")

		
number of vowels in given sentence is
number of vowels in given sentence is
number of vowels in given sentence is
number of vowels in given sentence is
number of vowels in given sentence is
>>> 
>>> sentence = input("enter the sentence:")
enter the sentence:AbeD
>>> string = sentence.lower()
>>> print(string)
abed
>>> count = 0
>>> list1 = ["a","e","i","o","u"]
>>> for char in string:
	if char in list1:
		count = count+1
		print("number vowels in given sentence is")

		
number vowels in given sentence is
number vowels in given sentence is
>>> 