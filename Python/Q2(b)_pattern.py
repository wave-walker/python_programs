row=int(input("Enter number of lines you want to print: "))
for i in range(1, row+1):
    if i > (row+1)/2:
        i = (row+1)-i
    # for space
    for j in range(1, row+1-i):
        print(' ', end='')

    # for increasing pattern
    for j in range(1, i+1):
        print(j, end='')

    # for decreasing pattern
    for j in range(i-1, 0, -1):
        print(j, end='')
    
    print()# Printing in new line