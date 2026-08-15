#Write a program to demonstrate a Floyd triangle pattern?
#Take input from user
rows = int(input("Please Enter the total Number of Rows: "))
number = 1 #initialize number to 1

print("Floyd's Triangle")
#outer loop for number of rows
for i in range(1, rows + 1):
    #inner loop for number of columns
    for j in range(1, i + 1):
        #display result
        print(number, end = ' ')
        number = number + 1

    print()

