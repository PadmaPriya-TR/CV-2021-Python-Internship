Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1) Create a function getting two integer inputs from user and perform arithmetic operations
>>> def operations(a,b):
	print("Addition of two numbers is",a+b)
	print("Subtraction of two numbers is",a-b)
	print("Multiplication of two numbers is",a*b)
	print("Division of two numbers is",a/b)

	
>>> print("Enter the numbers")
Enter the numbers
>>> a=int(input())
200
>>> b=int(input())
50
>>> operations(a,b)
Addition of two numbers is 250
Subtraction of two numbers is 150
Multiplication of two numbers is 10000
Division of two numbers is 4.0
>>> # Create a function covid() and it should accept patient name and body temperature
>>> def covid(name,temperature):
	print("Name of the patient: ",name)
	if temperature=="":
		print("Patient's body temperature is 98 degree")
	else:
		print("Patient's body temperature is",temperature, "degree")

		
>>> print("Enter patient's name:")
Enter patient's name:
>>> name=input()
Priya
>>> print("Enter patient's body temperature ")
Enter patient's body temperature 
>>> temperature=input()
105
>>> covid(name,temperature)
Name of the patient:  Priya
Patient's body temperature is 105 degree
>>> print("Enter patient's name:")
Enter patient's name:
>>> name1=input()
Padma
>>> print("Enter patient's body temperature ")
Enter patient's body temperature 
>>> temperature1=input()

>>> covid(name1,temperature1)
Name of the patient:  Padma
Patient's body temperature is 98 degree
>>> def covid(**details):
	print("Name of the patient: ",details["name"])
	if details["temperature"]=="":
		print("Patient's body temperature is 98 degree")
	else:
		print("Patient's body temperature is",details["temperature"], "degree")

		
>>> name2="Padma Priya"
>>> covid(name=name2,temperature="")
Name of the patient:  Padma Priya
Patient's body temperature is 98 degree
>>> 