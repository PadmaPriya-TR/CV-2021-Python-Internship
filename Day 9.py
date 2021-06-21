Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1) Write a program to loop through a list of numbers and add +2 to every value to elements in list
>>> List1=[]
>>> n=int(input("Enter the number of elements: "))
Enter the number of elements: 6
>>> print("Enter the elements: ")
Enter the elements: 
>>> for i in range(n):
	num=int(input())
	List1.append(num)

	
1
2
3
4
5
6
>>> print(List1)
[1, 2, 3, 4, 5, 6]
>>> for i in range(len(List1)):
	List1[i]+=2

	
>>> print(List1)
[3, 4, 5, 6, 7, 8]
>>> #2) Write a program to get the below pattern
>>> # 54321
>>> # 4321
>>> # 321
>>> # 21
>>> # 1
>>> n=int(input())
5
>>> for i in range(n,0,-1):
	j=i
	while j>0:
		print(j,end=" ")
		j=j-1
	print()

	
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
>>> #3) Python Program to Print the Fibonacci sequence
>>> n1=int(input("Enter the number of terms"))
Enter the number of terms 8
>>> a=0
>>> b=1
>>> sum=0
>>> count=1
>>> if n1<=0:
	print("Provide a positive integer")
elif n1==1:
	print("Fibonacci sequence: ", num1)
else:
	print("Fibonacci sequence: ", end=" ")
	while (count<=n1):
		print(sum, end=" ")
		count+=1
		a=b
		b=sum
		sum=a+b

		
Fibonacci sequence:  0 1 1 2 3 5 8 13 
>>> #4) Explain Armstrong number and write a code with a function
>>> # An Armstrong number is an integer such that sum of the cubes of its digits is equal to the number itself.
>>> number=int(input("Enter the number "))
Enter the number 153
>>> sum1=0
>>> temp=number
>>> while temp>0:
	digit=temp%10
	sum1+=digit**3
	temp//=10

	
>>> if number==sum1:
	print(number, "is an Armstrong number")
else:
	print(number, "is not an Armstrong number")

	
153 is an Armstrong number
>>> #5) Write a program to print the multiplication table of 9
>>> table=9
>>> for i in range(1,11):
	print(table,"x",i,"=",table*i)

	
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
>>> #6) Check if a program is negative or positive
>>> value=int(input("Enter the number "))
Enter the number -100
>>> if(value>0):
	print("The number is positive")
elif(value<0):
	print("The number is negative")
else:
	print("The number is 0")

	
The number is negative
>>> #7) Write a program to convert the number of days to ages
>>> days=int(input("Enter the number of days "))
Enter the number of days 7150
>>> print("Age is ",round((days/365),2))
Age is  19.59
>>> #8) Solve Trigonometry problem using math function write a program to solve using math function
>>> import math
>>> def trig_fnctn(choice,val):
	if choice==1:
		return math.sin(val)
	elif choice==2:
		return math.cos(val)
	elif choice==3:
		return math.tan(val)
	elif choice==4:
		return math.cosec(val)
	elif choice==5:
		return math.sec(val)
	elif choice==6:
		return math.cot(val)
	else:
		print("Enter a valid choice")

		
>>> print("Choose a number","\n","Enter 1 for sin","\n","Enter 2 for cos","\n","Enter 3 for tan","\n","Enter 4 for cosec","\n","Enter 5 for sec","\n","Enter 6 for cot")
Choose a number 
 Enter 1 for sin 
 Enter 2 for cos 
 Enter 3 for tan 
 Enter 4 for cosec 
 Enter 5 for sec 
 Enter 6 for cot
>>> choice=int(input())
2
>>> val=int(input("Enter the value: "))
Enter the value: 180
>>> trig_fnctn(choice,val)
-0.5984600690578581
>>> trig_fnctn(3,90)
-1.995200412208242
>>> #8) Create a calculator only on a code level by using if condition (Basic arithmetic calculation)
>>> def calculator(first_num,sec_num,oper):
	if oper==1:
		return first_num+sec_num
	elif oper==2:
		return first_num-sec_num
	elif oper==3:
		return first_num*sec_num
	elif oper==4:
		return round((first_num/sec_num),2)
	elif oper==5:
		return first_num**sec_num
	else:
		print("Enter a valid choice")

		
>>> first_num=eval(input("Enter the first number: "))
Enter the first number: 20
>>> sec_num=eval(input("Enter the second number: "))
Enter the second number: 10
>>> print("Choose a number","\n","Enter 1 for Addition","\n","Enter 2 for Subtraction","\n","Enter 3 for Multiplication","\n","Enter 4 for Division","\n","Enter 5 for Exponent")
Choose a number 
 Enter 1 for Addition 
 Enter 2 for Subtraction 
 Enter 3 for Multiplication 
 Enter 4 for Division 
 Enter 5 for Exponent
>>> oper=int(input("Select the operation: "))
Select the operation: 1
>>> calculator(first_num,sec_num,oper)
30
>>> calculator(40,5,3)
200
>>> 