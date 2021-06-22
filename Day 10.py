Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Account_Details:
	def __init__(self,num,name):
		self.acc_num=num
		self.acc_name=name
		self.acc_balance=0
		print("Hello",self.acc_name,"!!")

		
>>> class Deposit(Account_Details):
	def Deposit_amount(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.acc_balance += amount
		print("\n Rs.",amount,"is deposited in your account successfully!")

		
>>> class Withdrawal(Account_Details):  
	def Withdraw_amount(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.acc_balance>=amount:
		    self.acc_balance-=amount
		    print("\n Rs.",amount,"is withdrawn from your account successfully!")
		else:
		    print("\n Your account balance is insufficient to make withdrawal  ")

		    
>>> num=int(input('Enter your Account number:   '))
Enter your Account number:   12345678901
>>> name=(input('Enter your Name:   '))
Enter your Name:   Priya
>>> acc_det=Account_Details(num,name)
Hello Priya !!
>>> dep=Deposit(num,name)
Hello Priya !!
>>> dep.Deposit_amount()
Enter amount to be Deposited: 10000

 Rs. 10000.0 is deposited in your account successfully!
>>> wit=Withdrawal(num,name)
Hello Priya !!
>>> wit.Withdraw_amount()
Enter amount to be Withdrawn: 500

 Rs. 500.0 is withdrawn from your account successfully!
>>> wit.Withdraw_amount()
Enter amount to be Withdrawn: 50000

Your account balance is insufficient to make withdrawal  