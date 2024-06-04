'''
Meta interview
diagonal traversal of  Matrix


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
#row, column: 
#0,0 -> 
#0,1 -> 1,0 -> 
#1,1 

n=3
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
output = [1, 2, 4, 3, 5, 7, 6, 8, 9]
#row, column: 
#0,0 ->
#0,1 -> 1,0 ->
#0,2 -> 1,1 ->2,0 
#1,2 ->2,1
#2,2

n=4
A = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]]

#(row, column): 
#0,0 ->
#0,1 -> 1,0 ->
#0,2 -> 1,1 ->2,0 
#0,3 -> 1,2 ->2,1 -> 3,0
#1,3 -> 2,2 -> 3,1->
#2,3 ->3,2
#3,3
output = [1, 2, 5, 3, 6, 9, 4,7,10,13, 8, 11,14, 12, 15, 16]

def downwardDiagonal(A):
  output = []
  row = len(A)
  column = len(A[0])
  
  for c in range(column):
    co = c
    r = 0
    while co>=0:
      print(A[r][co], end=" ")
      r+=1
      co-=1
      
    print()
    
  for r in range(1, row):
    ro = r
    co=column-1
    #while co>=1 and ro>=row-1:
    while ro<=row-1:
      print(A[ro][co], end = " ")
      ro+=1
      co-=1
    print()
      
      
    
    
def downwardDiagonal(A):
  output = []
  row = len(A)
  column = len(A[0])
  
  for c in range(column):
    r = 0
    while c>=0:
      output.append(A[r][c])
      r+=1
      c-=1
      
 
    
  for r in range(1, row):
   
    c=column-1
    #while co>=1 and ro>=row-1:
    while r<=row-1:
      output.append(A[r][c])
      r+=1
      c-=1
  
      
      
  
  




