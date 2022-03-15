while True:
    def main():
        n=int(input("Enter your number: "))
        temp_save=n
        rev=0
        while(n>0):
            dig=n%10
            rev=rev*10+dig
            n=n//10
        if(temp_save==rev):
            print("The number is palindrome!")
        else:
            print("Not a palindrome!")
    if __name__=='__main__':
        main()