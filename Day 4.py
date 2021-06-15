Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1)Create three variables of same value
>>> a=b=c=200
>>> #Divide a by 10
>>> print(a/10)
20.0
>>> #Multiply b by 50
>>> print(b*50)
10000
>>> #Add c value by 60
>>> print(c+60)
260
>>> #2) Create a String variable of 5 characters and replace the 3rd character with G
>>> String="Priya"
>>> print(String.replace("i","G"))
PrGya
>>> #Aliter(Converting into list)
>>> String1="Priya"
>>> Strlist=list(String1)
>>> # 3rd character is at position 2 as index starts from 0
>>> Strlist[2]="G"
>>> String1="".join(Strlist)
>>> print(String1)
PrGya
>>> #3)Create two values of int,float data type & convert the vise versa
>>> a=5
>>> b=23.627
>>> print(float(a))
5.0
>>> print(int(b))
23
>>> 