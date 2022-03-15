# This program prints figure as shown below 
# 1 
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# 6 5 4 3 2 1
# 7 6 5 4 3 2 1
# 8 7 6 5 4 3 2 1
# 9 8 7 6 5 4 3 2 1

def pattern(rows):
    for row in range(1, rows):
        for column in range(row, 0, -1):
            print(column, end=' ')
        print()
def main():
    rows = int(input('Enter the number of rows you want to print: '))
    pattern(rows)
if __name__=='__main__':
    main()