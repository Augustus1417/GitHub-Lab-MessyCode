def Addition(num1,num2):
	return num1 + num2

def EnterNumber():
	try:
		num1 = int(input("Enter First Number: "))
		num2 = int(input("Enter Second Number: "))
	except:
		print("Please input numbers")
	return num1,num2


def main( ):
	print("This is a simple adder program")
	num1, num2 = EnterNumber() 
	result = Addition(num1, num2)
	print("The sum is :",result)

main()
