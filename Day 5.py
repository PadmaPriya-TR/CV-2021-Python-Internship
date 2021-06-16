Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1) Write a program to create list of n intergers values and do the following
>>> n=int(input('Enter the number of elemnts in the list '))
Enter the number of elemnts in the list 6
>>> List1=[]
>>> for i in range(n):
	element=int(input())
	List1.append(element)

	
2
4
6
12
1
3
>>> print(List1)
[2, 4, 6, 12, 1, 3]
>>> List1.sort()
>>> print(sorted(List1))
[1, 2, 3, 4, 6, 12]
>>> #Add an item into the list
>>> List1.append(7)
>>> print(List1)
[1, 2, 3, 4, 6, 12, 7]
>>> List1.insert(2,8)
>>> print(List1)
[1, 2, 8, 3, 4, 6, 12, 7]
>>> List2=[9,10,11,12]
>>> List1.extend(List2)
>>> print(List1)
[1, 2, 8, 3, 4, 6, 12, 7, 9, 10, 11, 12]
>>> # Delete operation
>>> del List1[2]
>>> print(List1)
[1, 2, 3, 4, 6, 12, 7, 9, 10, 11, 12]
>>> del List1[7:10]
>>> print(List1)
[1, 2, 3, 4, 6, 12, 7, 12]
>>> List1.remove(12)
>>> print(List1)
[1, 2, 3, 4, 6, 7, 12]
>>> item=List1.pop()
>>> print(List1)
[1, 2, 3, 4, 6, 7]
>>> print(item)
12
>>> item1=List1.pop(0)
>>> print(item1)
1
>>> item2=List1.pop(2)
>>> print(item2)
4
>>> print(List1)
[2, 3, 6, 7]
>>> # Store the Largest number from the list to a variable
>>> Large=max(List1)
>>> print(Large)
7
>>> Small=min(List1)
>>> print(Small)
2
>>> #2) Create a tuple and print the reverse of the created tuple
>>> Tuple1=(5,"Priya", 4.57, 2, "India", 9.8,'p')
>>> print(Tuple1[::-1])
('p', 9.8, 'India', 2, 4.57, 'Priya', 5)
>>> #3) Create a tuple and convert tuple into list
>>> List3=list(Tuple1)
>>> print(List3)
[5, 'Priya', 4.57, 2, 'India', 9.8, 'p']
>>> 