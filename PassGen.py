import random, os, sys, datetime
from sys import platform

def clearCLI():
	if platform == 'win32':
		os.system('cls')
	elif platform != 'win32':
		os.system('clear')

class passwordEngine():
	def __init__(self):
		self.passwords = []

	def generate(self, amount=1, length=8, complexity=1):
		complexity = complexity - 1
		complexity_list = []
		complexity_list.append('abcdefghijklmnopqrstuvwxyz')
		complexity_list.append('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
		complexity_list.append('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
		complexity_list.append('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_*&%$#@!-+/')

		for p in range(amount):
			password = ''
			for c in range(length):
				password += random.choice(complexity_list[complexity])
			self.passwords.append(password)
		return self.passwords

	def export(self, location=None):
		timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

		if location:
			file_name = location + 'Passwords_' + timestamp + '.txt'
		else:
			file_name = 'Passwords_' + timestamp + '.txt'

		with open(file_name, 'w') as f:
			for item in self.passwords:
				f.write("%s\n" % item)

def demo():
	passwords = passwordEngine().generate(amount=10, length=32, complexity=4)
	print('-' * 32)
	print('			  DEMO')
	print('-' * 32)
	for p in passwords:
		print (str(p))
	print('-' * 32)



def passGenCLI():
	passEn = passwordEngine()
	clearCLI()
	print('-' * 32)
	print('	   Password Generator')
	print('-' * 32)
	print('Complexity Level:')
	print('-' * 32)
	print('Weak	  1')
	print('Good	  2')
	print('Strong	3')
	print('Extreme   4')

	### Get Complexity form userInput
	complexity = 0
	while complexity == 0:
		print('-' * 32)
		userInput = input('Level of complexity? (Type the Number that is next to each level.) ')
		print('-' * 32)

		try:
			complexity = int(userInput)

			if complexity > 0 and complexity < 5:
				clearCLI()
				continue
			else:
				clearCLI()
				complexity = 0
				print('Invalid Entry: Must be between 1-4')
				continue
		except:
			clearCLI()
			print('Invalid Entry: Must be a number')
			continue

	### Get Length from User
	length = 0
	while length == 0 or length > 32:
		print('-' * 32)
		userInput = input('Length of Password? ')
		print('-' * 32)

		try:
			length = int(userInput)

			if length > 32:
				clearCLI()
				print('Invalid Entry: Can not be longer than 32 characters')
				continue
			elif length > 0 and length <= 32:
				clearCLI()
				continue
			elif length < 0:
				clearCLI()
				length = 0
				print('Invalid Entry: Must be greater than 0')
				continue
		except:
			clearCLI()
			print('Invalid Entry: Must be a number')
			continue

	### Get amount from User
	amount = 0
	while amount == 0:
		print('-' * 32)
		userInput = input('How many Passwords to generate? ')
		print('-' * 32)

		try:
			amount = int(userInput)

			if amount > 0:
				clearCLI()
				continue
			else:
				amount = 0
				clearCLI()
				print('Invalid Entry: Must be greater than 0')
				continue
		except:
			clearCLI()
			print('Invalid Entry: Must be a number')
			continue

	passwords = passEn.generate(amount, length, complexity)

	print('-' * 32)
	for p in passwords:
		print (str(p))
	print('-' * 32)
	save = input('Save generated password(s) to a file on this computer? (Type YES or NO) ').lower()

	if save == 'yes' or save == 'y':
		print('-' * 32)
		location = input('Location (Leave Blank to save in Current Directory) ').lower()
		if not location == '':
			passEn.export(location)
		else:
			passEn.export()

	if save == 'yes' or save == 'y':
		print('-' * 32)
		print('Passwords Saved.')
	print('-' * 32)
	again = input('Want more passwords? (Type YES for more passwords) ').lower()
	again = str(again)

	if again == 'yes' or again == 'y':
		clearCLI()
		passGenCLI()
	elif again == 'no':
		clearCLI()


if '--cli' in sys.argv:
	passGenCLI()
elif '--demo' in sys.argv:
	demo()
elif not '--demo' in sys.argv or '--cli' in sys.argv:
	print('Please type in --cli or --demo')
