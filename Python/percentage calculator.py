print('Simple Percentage Calulator')
p = int(input('Enter Your Physics Marks- '))
c = int(input('Enter Your Chemistry Marks- '))
m = int(input('Enter Your Biology Marks- '))
tMarks= p+c+m
if tMarks<=300:
    per= int((tMarks/300)*100)
    print('Your Percentage is ',per,'\b%')
else:
    print('CANNOT CALCULATE YOUR PERCENTAGE, SINCE THE GIVEN VALUES EXCEEDS MAXIMUM MARKS PARAMETERS\n')