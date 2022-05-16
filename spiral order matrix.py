
    ''' 
    Given an m x n matrix, return all elements of the matrix in spiral order. 
    k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''

def spiralOrder(matrix):

    res=[]
    left, right=0, len(matrix[0]) #right 6
    top, bottom =0, len(matrix) #bottom 3 ++
    while left<right and top<bottom:
        
        for i in range(left, right):
            res.append(matrix[top][i])
        top+=1
        
        for i in range(top,bottom):
            res.append(matrix[i][right-1])
            
        right-=1
        
        if not (left<right and top<bottom):
            break
        
#        if left<right:
        for i in range(right-1,left-1,-1):
            res.append(matrix[bottom-1][i])
        bottom-=1
            
        for i in range(bottom-1, top-1,-1):
            res.append(matrix[i][left])
        
        left+=1
    return res

matrix = [[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12],[13, 14, 15, 16, 17, 18]]






def spiralPrint(m, n, a):
    k = 0
    l = 0
 
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''
 
    while (k < m and l < n):
 
        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            print(a[k][i], end=" ")
        k += 1

        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            print(a[i][n - 1], end=" ")
        n -= 1
 
        # Print the last row from
        # the remaining rows
        if (k < m):
            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")
            m -= 1
 
        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")
            l += 1
 
# Driver Code
a = [[1, 2, 3, 4, 5, 6],
     [7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18]]
