# print('''Thus program prints serires like this: 
# 1
# 21
# 321
# 4321
# 54321 and so on... depending on user's input. Let's Give it a try''')
size= int(input("Enter the size of the series")) # It takes input for the size of the series.
i=1
while(i<=size): # first loop.
   j=i
   while(j>=1): # inner loop.
       print(j, end = ' ') # printin' the series.
       j=j-1
   i=i+1
   print("")  #ths gives a new line after every code block execution.




# printin' the series.
#ths gives a new line after every code block execution.