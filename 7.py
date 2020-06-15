#Three conditions hold:
#1. The position of next number is calculated by decrementing row number of previous number by 1, and incrementing the column number of previous number by 1. At any time, if the calculated row position becomes -1, it will wrap around to n-1. Similarly, if the calculated column position becomes n, it will wrap around to 0.
#2. If the magic square already contains a number at the calculated position, calculated column position will be decremented by 2, and calculated row position will be incremented by 1.
#3. If the calculated row position is -1 & calculated column position is n, the new position would be: (0, n-2). 

#Function
def generateSquare(n): 
    # 2-D array with all  
    # slots set to 0 
    magicSquare = [[0 for x in range(n)] 
                      for y in range(n)] 
    # initialize position of 1 
    i = n / 2
    j = n - 1
    # Fill the square by placing values 
    num = 1
    while num <= (n * n): 
        if i == -1 and j == n: # 3rd condition 
            j = n - 2
            i = 0
        else:  
            # next number goes out of 
            # right side of square  
            if j == n: 
                j = 0    
            # next number goes  
            # out of upper side 
            if i < 0: 
                i = n - 1
        if magicSquare[int(i)][int(j)]: # 2nd condition 
            j = j - 2
            i = i + 1
            continue
        else: 
            magicSquare[int(i)][int(j)] = num 
            num = num + 1
        j = j + 1
        i = i - 1 # 1st condition 
    # Printing the square 
    print ("Magic Square for n =", n) 
    print ("Sum of each row or column",n * (n * n + 1) / 2, "\n") 
    for i in range(0, n): 
        for j in range(0, n): 
            print('%2d ' % (magicSquare[i][j]),end = '') 
            # To display output  
            # in matrix form 
            if j == n - 1:  
                print()
# Driver Code 
# Works only when n is odd 
n=int(input("Number of rows of the Magic Square:"))
generateSquare(n)

