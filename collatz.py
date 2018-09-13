#Collatz Conjecture

def getNumber():
	"""
	This function gets a number as user input for the algorithm
	"""
	while True:
		try:
			number = int(input("Please enter a number bigger than 1:\n"))
		except:
			print("It seems like you did not enter a number.")
		else:
			if (number <= 1):
				print("You need to enter a number bigger than 1.")
				continue
			else:
				break
	return number

def getConjecture(number):
	"""
	For the Collatz Conjecture, we want to know how many steps it takes for a given number to reach 1.

	If the number is even, divide it by 2. If odd, multiply by 3 and add 1.
	"""
	# Declare count to store the number of steps needed
	count = 0
	while (number != 1):
		
		# If number is even, divide by 2
		if (number % 2 == 0):
			number /= 2
			count = count + 1
		# If number is odd, multiply by 3 and add 1
		else:
			number = number * 3 + 1

	return count


# Main
number = getNumber() # Get the number
count = getConjecture(number)
print(f"The number of steps needed is {count}")

