x = 5
mat = [
    [1,2,3],
    [4,5,8],
    [10,17,22],
]

n=len(mat)

def search(mat, n, x):
 
    i = 0
     
    # set indexes for top right element
    j = n - 1
    while ( i < n and j >= 0 ):
     
        if (mat[i][j] == x ):
     
            print("Element found at ", i, ", ", j)
            return True
     
        if (mat[i][j] > x ):
            j -= 1
             
        # if mat[i][j] < x
        else:
            i += 1
     
    print("Element not found")
    return False # if (i == n || j == -1 )
search(mat, n, x)



def practice(num, matrix):
    for i in matrix:
        if num in i:

            return True
        else: 
            continue
    
     return False
    
