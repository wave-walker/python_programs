# Printing half of the tuple in one line and the other half in the next line.
# ----------Part A------------
t1 = (1,2,5,7,9,2,4,6,8,10)
half_t1 = t1[:len(t1)//2]
anotherHalf_t1 = t1[len(t1)//2:]
print("The half of the given tuple t1: ", half_t1)
print("The another half of the given tuple t1: ", anotherHalf_t1)
print()
print()

# ----------Part B------------
# Tuple Even 
print("Given tuple: ", t1)

print("\nTherefore, the even numbers in this t1 Tuple are:")
for i in range(len(t1)):
    if(t1[i] % 2 == 0):
        # even_tuple=t1[i]
        print(t1[i], end = " ")
        # print(even_tuple, end = " ")
print()
print()

# ----------Part C------------
# concatenation of tuple
# given tuples named TUP (to prevent confilct)
t2 = (11, 13, 15)
tup_1 = (1,) #left with comma so that conflict between tuple b/w int will not occur
  
# printing original tuples
print("The original tuple 1: " + str(t2))
print("The original tuple 2: " + str(tup_1))
  
#concatenating tuples
resulting_tup  = t2 + tup_1
# printing result
print("The tuple after concatenation is : " + str(resulting_tup))
print()
print()
# ----------Part D------------
print("Concatenated tuple: ", resulting_tup)
tmax= max(resulting_tup)
tmin= min(resulting_tup)
print("Hence, the maximum value returned from this tuple is:",tmax,"\nand minimum value is:", tmin)
print('Program ended!')