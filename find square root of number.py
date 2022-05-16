'''
Google onsite interview 4
#Find the squareroot of a given number rounded down to the nearest integer, without using the sqrt function. 
For example, sqeuaroot of a number between [9,15] should return 3, and [16,24] should be 4
#THe squareroot of a (non-negative) number N alwasy lies between 0 and N/2. The straightforward way 
to solve this problem would be to check every number k between 0 and N/2, until the suqare of 
k becomes greater than or equal to N. if k^2 becomes equal to N, then we return k. 
Otherwise, we return k-1 because we're rounding down. 
'''
for k in range(1,3):
    print(k)

def solution(num):
    if num <0:
        return ValueError
    if num==1:
        return 1
    
    for k in range(round(num/2)+1):
        if k**2 == num:
            return k
        elif k**2> num:
            return k-1
    return k
        
solution(3)     


#binary search
def better_solution(num):
    if num <0:
        raise ValueError
    if num==1:
        return 1
    low = 0
    high = round(num/2+0.1)+1
#    high = round(num/2+0.1)    
    
#    while low+1<high:
#        mid = low + round((high-low)/2+0.1)
#        square = mid**2
#        if square ==num:
#            return mid
#        elif square < num:
#            low = mid
#        else:
#            high = mid
#    return low

    while low+1<high:
        mid = round((high+low)/2+0.1)
        square = mid**2
        if square ==num:
            return mid
        elif square < num:
            low = mid
        else:
            high = mid
    return low

better_solution(-1)
