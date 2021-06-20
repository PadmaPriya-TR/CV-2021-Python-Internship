Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #1
>>> dict1={"Priya":"CSE", "Mesh":"ECE", "Rosy":"Maths", "Nivi":"EEE", "Soorya": "MECH"}
>>> dict2={"Femee":"Biotech", "Rethu":"IT", "Abi":"English", "Ashi":"Physics", "Karthika": "Chemistry"}
>>> dict1.update(dict2)
>>> print(dict1)
{'Priya': 'CSE', 'Mesh': 'ECE', 'Rosy': 'Maths', 'Nivi': 'EEE', 'Soorya': 'MECH', 'Femee': 'Biotech', 'Rethu': 'IT', 'Abi': 'English', 'Ashi': 'Physics', 'Karthika': 'Chemistry'}
>>> #2
>>> List1=[2,34,11,56,21,8]
>>> List1.sort(reverse=True) #Descending order
>>> print(List1)
[56, 34, 21, 11, 8, 2]
>>> List1.sort() #Descending to Ascending
>>> print(List1)
[2, 8, 11, 21, 34, 56]
>>> Set1=set(List1) #Converting to set
>>> #3
>>> def count_key(dict1):
	count=0
	for i in enumerate(dict1):
		count+=1
	return count

>>> print(count_key(dict1))
10
>>> def displays_keys(dict1):
	for keys,values in dict1.items():
		print(keys,values,"\n")

		
>>> displays_keys(dict1)
Priya CSE 

Mesh ECE 

Rosy Maths 

Nivi EEE 

Soorya MECH 

Femee Biotech 

Rethu IT 

Abi English 

Ashi Physics 

Karthika Chemistry 

>>> print(sorted(dict1.keys()))
['Abi', 'Ashi', 'Femee', 'Karthika', 'Mesh', 'Nivi', 'Priya', 'Rethu', 'Rosy', 'Soorya']
>>> print(sorted(dict1.items()))
[('Abi', 'English'), ('Ashi', 'Physics'), ('Femee', 'Biotech'), ('Karthika', 'Chemistry'), ('Mesh', 'ECE'), ('Nivi', 'EEE'), ('Priya', 'CSE'), ('Rethu', 'IT'), ('Rosy', 'Maths'), ('Soorya', 'MECH')]
>>> def sortfn(dict1):
	ans=dict()
	min=dict1[key]
	for key in sorted(dict1):
		if dict1[key]<min:
			min=dict1[key]
			ans[key]=min
	return ans

>>> print(sortfn(dict1))
[('Abi', 'English'), ('Ashi', 'Physics'), ('Femee', 'Biotech'), ('Karthika', 'Chemistry'), ('Mesh', 'ECE'), ('Nivi', 'EEE'), ('Priya', 'CSE'), ('Rethu', 'IT'), ('Rosy', 'Maths'), ('Soorya', 'MECH')]
>>>#4
>>> String1=input()
Everyday is a good day. Everyday is a new beginning
>>> old=input()
Everyday is
>>> new=input()
Have
>>>String1.replace(old,new,1)
'Have a good day. Everyday is a new beginning'
#5)
>>> String4=input()
betty botter bought some butter but the butter it was bitter if she put it in her batter it would make her batter bitter but a bit of better butter that would make her batter better
>>> def char_upper(String4):
	c=String4[0]
	String4=String4.replace(c,c.upper())
	String4=c+String4[1:]
	return String4

>>> print(char_upper(String4))
betty Bought some Butter But the Butter was Bitter
>>> List3=["Priya","Padma","Priya","Mesh","Siva","Raji","Mesh"]
>>> List4=[]
>>> for i in range(0, len(List3)):
	for j in range(i+1, len(List3)):
		if(List3[i]==List3[j]):
			List4.append(List3[j])
>>> print("The repeated  items of a list are ",List4)
The repeated  items of a list are  ['Priya', 'Mesh']
>>>#6
>>> a=int(input("Enter the first number"))
Enter the first number 4
>>>  b=int(input("Enter the second number "))
Enter the first number 12
>>> c=int(input("Enter the third number "))
Enter the third number 24
>>> sum=a+b+c
>>> print("The sum of the numbers is ",sum)
The sum of the numbers is  40
>>> divide=int(input("Enter the number to divide "))
Enter the number to divide 10
>>> if sum%divide==0:
	print("Divisible")
else:
	print("Not Divisible")

	
Divisible
>>>mean=float(sum/3)
>>> print(mean)
13.333333333333334
>>> num_lst=[a,b,c]
>>> if len(num_lst)%2==0:
	median1=num_lst[len(num_lst)//2]
	median2=num_lst[len(num_lst)//2-1]
	median=(median1+median2)/2
else:
	median=num_lst[len(num_lst)//2]
>>> print("Median is",median)
Median is 12
>>> import collections
>>> data=collections.Counter(num_lst)
>>> data_lst=dict(data)
>>> max_value=max(list(data.values()))
>>> mode_val=[num for num, freq in data_lst.items() if freq==max_value]
>>> if len(mode_val)==len(num_lst):
	print("No mode")
else:
	print("The mode is: "join(map(str, mode_val))
	      
No mode
#9
>>> strcase=input("Enter the string")
Enter the string Python ProgramminG
>>> def swap_case(strcase):
	result=""
	for item in strcase:
		if item.isupper():
			result+=item.lower()
		else:
			result+=item.upper()
	return result

>>> print(swap_case(strcase))
 pYTHON pROGRAMMINg
#10
>>> def dectobin(num):
	bin=[0]*num
	i=0
	while(num>0):
		bin[i]=num%2
		num=int(num/2)
		i+=1
	for j in range(i-1,-1,-1):
		print(bin[j], end=" ")
>>> def dectooct(num1):
	oct=[0]*num1
	i=0
	while(num1!=0):
		oct[i]=num1%8
		num1=int(num1/8)
		i+=1
	for j in range(i-1,-1,-1):
		print(oct[j], end=" ")
>>> num=int(input("Enter the number"))
Enter the number7
>>> dectobin(num)
1 1 1 
>>> num=int(input("Enter the number"))
Enter the number33
>>> dectooct(num)
4 1 
>>> 