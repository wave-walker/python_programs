# To find the L.C.M. of two numbers using python

def lcm(a, b):
   # choosing the greater number
   if a > b:
       greater = a
   else:
       greater = b
   while(True):
       if((greater % a == 0) and (greater % b == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

def main():
    a = int(input("Enter your first number: "))
    b = int(input("Enter the second number: "))
    print("The L.C.M. is", lcm(a, b))
    lcm(a, b)

if __name__=='__main__':
    main()