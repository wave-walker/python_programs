# To check if a string is palindrome or not
def palindrome():
    user_str = input('Enter a string to check whether it is a palindrome or not:  ') 
    # reversing the string 
    str_reversed = reversed(user_str)

    #  comparing wtth the help of list functions that will convert them into list and check if they are equal to its reverse
    if list(user_str) == list(str_reversed): 
       print("The string is a palindrome.")
    else:
       print("The string is not a palindrome.")
if __name__=='__main__':
    palindrome()