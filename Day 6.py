Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1) Write a python script to merge two python dictionaries
>>> dict1={"Priya":"CSE", "Mesh":"ECE", "Rosy":"Maths", "Nivi":"EEE", "Soorya": "MECH"}
>>> dict2={"Femee":"Biotech", "Rethu":"IT", "Abi":"English", "Ashi":"Physics", "Karthika": "Chemistry"}
>>> dict1.update(dict2)
>>> print(dict1)
{'Priya': 'CSE', 'Mesh': 'ECE', 'Rosy': 'Maths', 'Nivi': 'EEE', 'Soorya': 'MECH', 'Femee': 'Biotech', 'Rethu': 'IT', 'Abi': 'English', 'Ashi': 'Physics', 'Karthika': 'Chemistry'}
>>> #2) Write a python program to remove a key from a dictionary
>>> del dict2["Ashi"]
>>> print(dict2)
{'Femee': 'Biotech', 'Rethu': 'IT', 'Abi': 'English', 'Karthika': 'Chemistry'}
>>> #3) Write a python program to map two lists into a dictionary
>>> List1=("Name","Department", "CGPA")
>>> List2=("Padma", "CSE", 9.5)
>>> Dict3=dict(zip(List1,List2))
>>> print(Dict3)
{'Name': 'Padma', 'Department': 'CSE', 'CGPA': 9.5}
>>> #4) Write a python program to find the length of a set
>>> set1=set()
>>> set1.add("India")
>>> set1.add("China")
>>> set1.add("Russia")
>>> set1.add("America")
>>> print("The length of the set is ",len(set1))
The length of the set is  4
>>> #5) Write a python program to remove the intersection of 2nd set from the first set
>>> set2={1,2,3,4,5}
>>> set3={3,4,5,6,7}
>>> set2.difference_update(set3)
>>> print(set2)
{1, 2}
>>> print(set3)
{3, 4, 5, 6, 7}
>>> 