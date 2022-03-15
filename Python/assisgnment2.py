import math
# print("This is /n ----", 'hello','\n','world')
# print("This is /a ----", 'hello','\a','world')
# print("This is /b ----", 'hello','\b','world')
# print("This is /r ----", 'hello','\r','world')
# print("This is /f ----", 'hello','\f','world')

# import random
# hell=random.random()
# print(hell)
#QUE 4

# def main(): # Also can be def hell(): function name could be anything also call that funtion with that name
#     print('Que no 4(a)')
#     print('          *')
#     print('     *    *    *')
#     print('*    *    *    *    *')
#     print('     *    *    *')
#     print('          *')
#     print('Que no 4(b)')
#     print('Now square wil be printed ')
#     print('$  $  $  $  $')
#     print('$           $')
#     print('$           $')
#     print('$           $')
#     print('$  $  $  $  $')
# def test(a, b)
#     a = a+b
#     b = a-b
#     a = a-b
#     print('a = ', a)
#     print('b = ', b)
# QUE 7
def areaTriangle(side1,side2,side3):
    s=(side1+side2+side3)/2  #Heron's formula to calculate area of triangle using sides
    d=s*(s-side1)*(s-side2)*(s-side3) #Heron's formula to calculate area of triangle using sides
    a=math.sqrt(d)
    return a
def main():
    side1=eval(input("Enter first side of triangle-----"))
    side2=eval(input("Enter second side of triangle-----"))
    side3=eval(input("Enter third side of triangle-----"))
    assert ((side1+side2)>side3) and ((side1+side3)>side2) and ((side2+side3)>side1)
    ans=areaTriangle(side1,side2,side3)
    print("Area: ",ans)

if __name__=='__main__':
   main()
# mine
# def aTriangle():
#     a= int(input('Enter Your Side 1--- '))
#     b= int(input('Enter Your Side 2--- '))
#     c= int(input('Enter Your Side 3--- '))
#     condition= a+b>c and b+c>a and c+a>b
#     if condition == True:
#         s= (a+b+c)/2 #s is semi perimeter)
#         area=((s*(s-a)*(s-b)*(s-c))**0.5)
#         print('\nThe area of given triangle is', area, 'sq. units')
#     else:
#         print('\nA triangle with these measurements is not possible ')

# if __name__=='__main__':
#     aTriangle()
# print('End of the program!\nThank you :)')