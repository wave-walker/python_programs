# This program prints figure as shown below 
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9
# 10 10 10 10 10 10 10 10 10 10 

def pattern():
    n= int(input("Enter a number: "))
    for n in range(1,n+1):
        print() #This prints a new line after every "i" loop execution
        for j in range(1, n+1):
            print(n, end=" ")
    print("\nEnd of the program! ")
if __name__=='__main__':
    pattern()