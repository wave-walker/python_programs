def sum_of_odds(n):
	return n*n #Formula to calculate sum of odd terms is given by n^2. I've verified it :)
n = int(input("Enter no. terms of odd numbers: "))
for i in range (1,2*n,2):
	print(i, end=' ') #Printing entered terms
# Escaping the loop pf printing nums

print() #A new line before answer
print("Hence, the sum of entered odd terms is given by ",sum_of_odds(n),'\n')


if __name__=='__main__':
	sum_of_odds(n)