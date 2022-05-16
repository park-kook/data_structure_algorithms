
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
