def fig():
    n=int(input("Enter the Number of pattern character"))
    for i in range(1,n+1):
        if i==1 or i==n:
            print(i)
if __name__=='__main__':
    fig()