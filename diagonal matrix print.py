



'''
Meta interview
diagonal traversal of Matrix


Give a N * N square matrix, return all the elements of its anti-diagonals from top to bottom.
N=2
Topmost anti-diagonal is [[1, ], 
                          [ , ]]
Next anti-diagonal is [[ , 2], 
                       [3,  ]]
and the last anti-diagonal is [[ ,  ], 
                               [ , 4]]
Hence, elements will be returned in the 
order {1, 2, 3, 4}.



Expected Time Complexity: O(N*N)
Expected Auxillary Space: O(N*N)
'''
n=2
A = [[1,2],
     [3,4]]
output = [1, 2, 3, 4]
#row, column: 0,0 -> 0,1 -> 1,0 -> 1,1 

n=3
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
output = [1, 2, 4, 3, 5, 7, 6, 8, 9]


n=4
A = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]
#row, column: 
#0,0 
#-> 0,1 -> 1,0 
#->0,2 -> 1,1 ->2,0 
#-> 1,2 ->2,1
#->2,2

def downwardDigonal(n,A):
    c=[]
    for l in range(2*n-1):
        t,b = max(0,l+1-n), min(l,n-1) # t=0, b=0 | t=
        
        for i in range(t, b+1):
            c.append(A[i][l-i])
        
    return c
downwardDigonal(n,A)

def downwardDigonal(n,A): #upper left and diagonal
    output =[]
    for col in range(n): #0,1,2
        j=col
        row=0
        while j>=0:

            output.append(A[row][j])
            
            row+=1
            j-=1
#    return output            
    for row in range(1,n): #lower right
        i=row
        col=n-1
        while i<n:

            output.append(A[i][col])
            col-=1
            i+=1
    return output
downwardDigonal(n,A)




# Python3 program to print all elements
# of given matrix in diagonal order
ROW = 5
COL = 4
#Time Complexity: O(row x col) 
#Auxiliary Space: O(1) 
# Main function that prints given
# matrix in diagonal order from bottom to top
'''
1
5 2
9 6 3
13 10 7 4
17 14 11 8
18 15 12
19 16
20
'''
 
def diagonalOrder(matrix):
 
    # There will be ROW+COL-1 lines in the output
    for line in range(1, (ROW + COL)):
        # Get column index of the first element
        # in this line of output. The index is 0
        # for first ROW lines and line - ROW for
        # remaining lines
        start_col = max(0, line - ROW)
 
        # Get count of elements in this line.
        # The count of elements is equal to
        # minimum of line number, COL-start_col and ROW
        count = min(line, (COL - start_col), ROW)
 
        # Print elements of this line
        for j in range(0, count):
            print(matrix[min(ROW, line) - j - 1]
                        [start_col + j], end="\t")
 
        print()
 
 
# Utility function to print a matrix
def printMatrix(matrix):
    for i in range(0, ROW):
        for j in range(0, COL):
            print(matrix[i][j], end="\t")
 
        print()
 
 
# Driver Code
M = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16],
     [17, 18, 19, 20]]
print("Given matrix is ")
printMatrix(M)
 
print("\nDiagonal printing of matrix is ")
diagonalOrder(M)
 
# This code is contributed by Nikita Tiwari.
