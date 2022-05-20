'''

Complexity Analysis: 
Time Complexity :O(n*k*log(n*k)). 
since resulting array is of N*k size.
Space Complexity :O(n*k), The output array is of size n*k.
'''


def mergeKArrays(arr,n,k,output):
    c=0
    output=[]
    
    for i in range(k):
        for j in range(n):
            output.append((arr[i][j]))
#            c+=1
    output.sort()
    
    return output

k=3
n=4
arr=[[2,6,12,34], [1,9,20,1000], [23,24, 90, 2000]]
output = [0 for i in range(n*k)]
mergeKArrays(arr,n,k, output)


