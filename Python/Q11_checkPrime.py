# Q11 program to check if a number is prime or not
def check_prime(num):
	if num > 1: # checking positivity of number
		for i in range(2,num):	# checking for factors
			if (num % i) == 0:
				print(num,"is not a prime number")
				print(i,"times",num//i,"is",num) #Shows the first factor of entered number (if persists any)
				break
		else:
			print(num,"is a prime number") #Result after implementation of all operations
	else: # If input parameter is less than or equal to 1, it is not prime
		print(num,"is not a prime number")

def main():
	num=int(input("Enter your number: "))
	check_prime(num)
if __name__=='__main__':
	main()