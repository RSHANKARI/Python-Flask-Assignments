Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #string occurence
>>> st = 'Happy eduyear'
>>> print(st.count('y'))
2
>>> 
>>> #even indexed
>>> st = 'eduyear'
>>> print(st[0 : len(st) : 2])
euer
>>> 
>>> #swapcase
>>> name="EdUyEaR"
>>> st = name.swapcase()
>>> print(name)
EdUyEaR
>>> print(st)
eDuYeAr
>>> 