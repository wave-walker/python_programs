def sum_of_evens(n):
	return n*(n+1) #Formula to calculate sum of even terms is given by n^2. I've verified it :)
n = int(input("Enter no. terms of even numbers: "))
for i in range (2,(2*n)+1,2):
	print(i, end=' ') #Printing entered terms
# Escaping the loop pf printing nums

print() #A new line before answer
print("Hence, the sum of entered even terms is given by ",sum_of_evens(n),'\n')


if __name__=='__main__':
	sum_of_evens(n)