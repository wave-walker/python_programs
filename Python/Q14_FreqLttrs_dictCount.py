#This function takes a sentence as input from the user and calculates the frequency of each letter.

# input string
user_str = input("Enter your string to check frequency of each letter in it: ")

# variable of dictionary type to maintain the count.
initialized_dict = {}

for i in user_str: #checking membership of i in input string and comparing it with whther it contains same in initialized_dict
	if i in initialized_dict:
		initialized_dict[i] += 1 #it will keep finding and addup freq until no repeated letter is left
	else:
		initialized_dict[i] = 1 #if not found then keep freq one

print ("Count of all characters in",user_str,"is :\n " + str(initialized_dict)) #result