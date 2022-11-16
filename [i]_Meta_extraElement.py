A = [10,15,5]
B = [10,5,100,15]


def extraElement(A,B):
  ans = 0
  
  for i in range(len(A)):
    ans ^=A[i]
  for i in range(len(B)):
    ans ^=B[i]
    
  return ans

extraElement(A,B)
                
