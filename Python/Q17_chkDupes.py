listOfElems=[1,51,46,12,1,2,2,98]
def check_duplicates():
	listOfElems=[1,51,46,12,1,2,2,98]
	# listOfElems=list(input("Enter a list: "))
	if len(listOfElems) == len(set(listOfElems)):
		print('So far we have searched but no duplicates were found...')
	else:
		print('This list contains duplicates.')

def frequency_of_duplicate():
	user_list = listOfElems
	initialized_dict = {}
	for i in user_list: #checking membership of i in input string and comparing it with whther it contains same in initialized_dict
		if i in initialized_dict:
			initialized_dict[i] += 1 #it will keep finding and addup freq until no repeated element is left
		else:
			initialized_dict[i] = 1 #if not found then keep freq one
	print ("\nCount of all duplicates in",user_list,"is :\n " + str(initialized_dict)) #result

if __name__=='__main__':
	check_duplicates()
	frequency_of_duplicate()