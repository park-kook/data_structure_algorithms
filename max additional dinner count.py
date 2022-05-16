
from typing import List
def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    output=[1]*(N+K) 
    for seat in S:
        i = seat-K-1
        while i <= seat+K-1:
            output[i]=0
            i+=1
    del output[N:]        

    newlist = []
    templist = []
    for i in output:
        if i == 0:
            newlist.append(templist)
            templist = []
        else:
            templist.append(i)        
    newlist.append(templist)
    
    count=0
    for i in newlist:
        for j in range(0,len(i),K+1):
#            if i[j] == 1:
                count+=1
    return count          
sum(output)

output[-1]  
i=[]
N=20
K=5
S=[5,17]       

N=10
K=1
S=[5] 
getMaxAdditionalDinersCount(20,5,2,[5,17]) 
