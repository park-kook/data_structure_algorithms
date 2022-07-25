'''
#Apple questions
#subscription business (apple music, Amazon prime video, Amzaon membership, etc.)
#cancel, inactive user, failed to pay for all churn population = churn 

#[1, 1, 2, 3, 3] => 2
#[1, 2, 2, 3, 3] => 1
#[1, 1, 3, 3, 5] => 5
#[1] =>1
#[1, 1, 3, 3, 5, 5, 7]
# [1, 1, 5, 5, 100, 100, 101, ..... ]
# 1000 =>  
#     mapSize < N
#     mapSize > N / 2 
# O(n/2)
#log n is much smaller than O(n/2)

Like the original array, after a pair from the center,
the subarray containing the single element must be odd-lengthed.
The subarray not containing it must be even-lengthed. 
So by taking a pair out of the middle and then calculating which side is now odd-lengthed, 
we have the information needed for binary search.
'''
1//2 #0
arr = [1, 1, 3, 3, 5, 5, 7] #odd middle
arr = [1, 1, 2, 3, 3] #even in middle
arr = [1, 2, 2, 3, 3] #even in middle
arr = [1, 1, 3, 3, 5] #even in middle
arr = [1]
arr = [1, 1, 3, 3, 5, 7, 7] #odd
arr = [1, 1, 3, 3, 5,5, 7, 7,8] #odd
arr = [1, 1, 3, 3, 7, 7, 8, 9, 9]
arr = [1, 1, 2, 3, 3, 5, 5, 7, 7]
        
def identify_outlier(arr):
    left = 0
    right = len(arr)-1
    if len(arr)==1:
        return arr[0]
    if arr[left]!=arr[left+1]:
        return arr[left]

    if arr[right]!=arr[right-1]:
        return arr[right]
    
    while left < right:
        mid = left + (right-left)//2

        if mid % 2 ==0:
            if arr[mid] != arr[mid+1]:
                return arr[mid]
            else:
                
                left = mid + 1
        else: 
            if arr[mid]!=arr[mid-1]:
                return arr[mid-1]
            else: 
                left = mid + 1
print(identify_outlier(arr))  
