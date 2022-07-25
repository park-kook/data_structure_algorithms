
A = [ 10, 15, 5 ]
B = [ 10, 100, 15, 5 ]
output = 100

A = [2, 4, 6, 8,  10, 12, 13]
B = [2, 4, 6, 8, 10, 12]

output=13

def findExtra(A, B):
    A.sort()
    B.sort()
    if len(A) <len(B):
        A,B=B,A
    for i in range(len(B)):
        if A[i] != B[i]:
            return A[i]
                     
    return A[len(A)-1]
  
  
  
  def extraElement(A, B):
 
    # To store the result
    ans = 0
 
    # Find the XOR of all the element
    # of array A[] and array B[]
    for i in range(len(A)):
        ans ^= A[i];
    for i in range(len(B)):
        ans ^= B[i];
    return ans
 
