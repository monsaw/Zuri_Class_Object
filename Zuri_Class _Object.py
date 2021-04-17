class Budget():
	"""
	A Program to run Budget of some categories based on User Request. (Food, Clothing,Entertainment)
	
	Carrying out functionalities such as 
		1. Depositing
		2. Withdrawing
		3. Transfering fund from one categories to another
	
	
	"""
	def __init__(self,food,clothing,entertainment):
		self.food=food
		self.clothing=clothing
		self.entertainment=entertainment
	
	def welcome(self):
		print()
		print('-'*65)
		print('\t\tWelcome to Budget Category Program')
		print('-'*65)
		print('Please choose a choice to perform')
		choose= int(input('\n\t1. Deposit \n\t2. Withdraw \n\t3. Transfer \n'))
		if choose == 1:
			self.deposit()
		elif choose == 2:
			self.withdraw()
		elif choose == 3:
			self.transfer()
		else:
			print('Invalid input, re-enter your choice ')
			self.welcome()
	def deposit(self):
		print('Please select an option in the categories to deposit into \n')
		print('\t 1.  Food\n\t 2.  Clothing \n\t 3.  Entertainment')
		selection=int(input())
		if selection == 1:
			value = int(input('Enter the amount to deposit to food category : '))
			self.food +=value
			print(f'You have successfully deposited #{value} into Food category \n')
			self.welcome()
		elif selection == 2:
			value = int(input('Enter the amount to deposit into Clothing category : '))
			self.clothing +=value
			print(f'You have successfully deposited #{value} into clothing category \n')
			self.welcome()
		elif selection ==3:
			value = int(input('Enter the amount to deposit into Entertainment category : '))
			self.entertainment +=value
			print(f'You have successfully deposited #{value} into entertainment category \n')
			
			self.welcome()
		else:
			print('Invalid Selection, Please input valid option : ')
			self.deposit()
			
	def withdraw(self):
		print('Please select an option in the categories to Withdraw from \n')
		print('\t 1.  Food\n\t 2.  Clothing \n\t 3.  Entertainment')
		selection=int(input())
		if selection == 1:
			amount= int(input('Enter the amount to Withdraw from Food Category : '))
			if amount > self.food:
				print(f'You do not have upto {amount} in your account ')
				change_option = input('Do you wish to take withdraw again? : Yes or No ').lower()
				if change_option == 'yes':
					self.withdraw()
				elif change_option == 'no':
					self.welcome()
				else:
					print('The selected invalid choice, you are exited of the program, Thanks')
					exit()
			else:
				self.food -=amount
				print(f'You have withdrawn #{amount} from your balance, you have #{self.food} left  ')
				print('Do you want to do further transaction? Yes or No :  ')
				Further = input().lower()
				if Further == 'yes':
					self.welcome()
				else:
					print('Thanks, Bye')
					exit()
					
		elif selection == 2:
			amount= int(input('Enter the amount to Withdraw from Clothing Category : '))
			if amount > self.clothing:
				print(f'You do not have upto {amount} in your account ')
				change_option = input('Do you wish to take withdraw again? : Yes or No ').lower()
				if change_option == 'yes':
					self.withdraw()
				elif change_option == 'no':
					self.welcome()
				else:
					print('The selected invalid choice, you are exited of the program, Thanks')
					exit()
			else:
				self.clothing -=amount
				print(f'You have withdrawn #{amount} from your balance, you have #{self.clothing} left  ')
				print('Do you want to do further transaction? Yes or No :  ')
				Further = input().lower()
				if Further == 'yes':
					self.welcome()
				else:
					print('Thanks, Bye')
					exit()
		elif selection ==3:
			amount= int(input('Enter the amount to Withdraw from Entertainment Category : '))
			if amount > self.food:
				print(f'You do not have upto {amount} in your account ')
				change_option = input('Do you wish to take withdraw again? : Yes or No ').lower()
				if change_option == 'yes':
					self.withdraw()
				elif change_option == 'no':
					self.welcome()
				else:
					print('The selected invalid choice, you are exited of the program, Thanks')
					exit()
			else:
				self.entertainment -=amount
				print(f'You have withdrawn #{amount} from your balance, you have #{self.entertainment} left  ')
				print('Do you want to do further transaction? Yes or No :  ')
				Further = input().lower()
				if Further == 'yes':
					self.welcome()
				else:
					print('Thanks, Bye')
					exit()
			
	def transfer(self):
		print('You have chosen to Transfer Funds from catergories')
		print('Choose Categories to transfer From')
		from_ = int(input('\n\t1. Food\n\t2. Clothing\n\t3. Entertainment \n'))
		print('Choose Categories to transfer To')
		to_ = int(input('\n\t1. Food\n\t2. Clothing\n\t3. Entertainment \n'))
		amount_transfered = int(input('Enter the amount to transfer : '))
			
		if from_ ==1 and to_ ==2:
			if amount_transfered > self.food:
				print(f'You do not have upto #{amount_transfered} in your Food savings, please retry \n')
				self.transfer()
			else:
				self.food -=amount_transfered
				self.clothing += amount_transfered
				print(f'You have succefully transfered #{amount_transfered} from Food savings to Clothing savings')
				print(f'Your current Food savings is #{self.food} while your current Clothing savings is #{self.clothing}\n')
				self.welcome()
				
		elif from_ ==1 and to_ ==3:
			if amount_transfered > self.food:
				print(f'You do not have upto #{amount_transfered} in your Food savings, please retry \n')
				self.transfer()
			else:
				self.food -=amount_transfered
				self.entertainment += amount_transfered
				print(f'You have succefully transfered #{amount_transfered} from Food savings to Entertainment savings')
				print(f'Your current Food savings is #{self.food} while your current Entertainment savings is #{self.entertainment}\n')
				self.welcome()
				
		elif from_ ==2 and to_ ==1:
			if amount_transfered > self.clothing:
				print(f'You do not have upto #{amount_transfered} in your Clothing savings, please retry \n')
				self.transfer()
			else:
				self.clothing -=amount_transfered
				self.food += amount_transfered
				print(f'You have succefully transfered #{amount_transfered} from Clothing savings to Food savings')
				print(f'Your current Clothing savings is #{self.clothing} while your current Food savings is #{self.food}\n')
				self.welcome()
				
		elif from_ ==2 and to_ ==3:
			if amount_transfered > self.clothing:
				print(f'You do not have upto #{amount_transfered} in your Clothing savings, please retry \n')
				self.transfer()
			else:
				self.clothing -=amount_transfered
				self.entertainment += amount_transfered
				print(f'You have succefully transfered #{amount_transfered} from Clothing savings to Entertainment savings')
				print(f'Your current Clothing savings is #{self.clothing} while your current Food savings is #{self.entertainment}\n')
				self.welcome()
				
		elif from_ ==3 and to_ ==1:
			if amount_transfered > self.entertainment:
				print(f'You do not have upto #{amount_transfered} in your Entertainment savings, please retry \n')
				self.transfer()
			else:
				self.entertainment -=amount_transfered
				self.food += amount_transfered
				print(f'You have succefully transfered #{amount_transfered} from Entertainment savings to Food savings')
				print(f'Your current Entertainment savings is #{self.entertainment} while your current Food savings is #{self.food}\n')
				self.welcome()
				
		elif from_ ==3 and to_ ==2:
			if amount_transfered > self.entertainment:
				print(f'You do not have upto #{amount_transfered} in your Entertainment savings, please retry \n')
				self.transfer()
			else:
				self.entertainment -=amount_transfered
				self.clothing += amount_transfered
				print(f'You have succefully transfered #{amount_transfered} from Entertainment savings to Clothing savings')
				print(f'Your current Entertainment savings is #{self.entertainment} while your current Clothing savings is #{self.clothing}\n')
				self.welcome()
				
		else:
			print('Invalid Transfer Request! \n ')
			self.transfer()
				

# Initiation of Class with default values for each categories.	
Monsaw = Budget(400,400,400)
Monsaw.welcome()
		
			