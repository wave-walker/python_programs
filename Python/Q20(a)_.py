
print('-------part a-------')
# Test if all elements in list are of same type i.e. numbers


# user inputed list
# user_list = [ 11,1,4,3,4,56,7,'9P']
user_list = [ 'kdlghjghjfg', '9P']

# printing original list
print("The original list is : " + str(user_list))

# Test if all elements in list are of same type using loop + isinstance()
result = True
for elements in user_list:
	if not isinstance(elements, type(user_list[0])):
		result = False
# printing result
print ("Do all elements have same type : " + str(result))


print('-------part b-------')
# To count Even and Odd numbers in a List

# list of numbers
# list1 = [10, 21, 4, 45, 66, 93, 11]
if int in user_list:
	even_count, odd_count = 0, 0
	num = 0

	# using while loop	
	while(num < len(user_list)):

		# checking condition
		if user_list[num] % 2 == 0:
			even_count += 1
		else:
			odd_count += 1

		# increment num
		num += 1

	print("Even numbers in the list: ", even_count)
	print("Odd numbers in the list: ", odd_count)


print('-------part c-------')
# Longest String in list using loop
if str in user_list:
	print("The original list: " + str(user_list))
	# Longest String in list using loop
	max_len = -1
	for ele in user_list:
		if len(ele) > max_len:
			max_len = len(ele)
			res = ele
	# printing result
	print("Maximum length string is : " + res)

print('-------part d-------')
# reverse the order of list elements
print('Given list: ', user_list)
user_list.reverse()
print('Reversed List:', user_list)

print('-------part e-------')


print('-------part d-------')