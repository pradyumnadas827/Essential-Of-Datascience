n = int(input("Enter a number: ")) #taking input

for i in range(0, n):  #loop from 0 to n-1
    for j in range(0, i+1 ): #loop from 0 to i to print the stars in each row
        print("*", end=" ")  #print a star and stay on the same line
    print( )  #print a new line after each row of stars is printed