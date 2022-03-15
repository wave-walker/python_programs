def len_str():
    print('You chose to find the length of your entered string')
    user_string= input("Enter your string: ")
    print(len(user_string))

def max_of_3_str():
    print('You have to enter three strings and maximum of three strings will be returned')
    user_string1= input("Enter your string 1: ")
    user_string2= input("Enter your string 2: ")
    user_string3= input("Enter your string 3: ")
    print(max(user_string1, user_string2, user_string3))

def replace_successive_character_with_hash():
    print('You have to enter a string and replace every successive character with #')
    user_string= input("Enter your string: ")
    ch=[]
    for i in user_string:
        ch.append(i)
    for j in range(1,len(ch),2):
        ch[j]= '#'
    output_string=''
    for k in ch:
        output_string=output_string+k
    print(output_string)

def no_of_wrds_in_str():
    print('You chose to find number of words in the your entered string')
    user_string= input("Enter your string: ")
    cnvrt_lst=list(user_string)
    a=len(cnvrt_lst)
    print("Hence, number of words in the entered string: ", a)

def main():
    print("\nThis is menu driven program that perform the following functions on strings\nChoose from the following:-1. Find the length of string\n 2. Return maximum of three strings\n 3. Accept a string and replace every successive character with #\n 4. Find number of words in the given string\n")
    x=int(input("To operate a function of yo    ur string, enter the relevant number from the menu: "))
    if x==1:
        len_str()
    elif x==2:
        max_of_3_str()
    elif x==3:
        replace_successive_character_with_hash()
    elif x==4:
        no_of_wrds_in_str()
    else:
        print("Invalid input! Please try again. Program terminated...\n")
if __name__=='__main__':
    main()