'''
#Apple questions
single element in a sorted array
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


O(N)
arr = [1, 4, 2, 1, 3, 2, 3]
def find_single_number(arr):
    num = 0
    for i in arr:
        num ^= i
    return num
find_single_number(arr)
'''
Recall the following two properties of XOR:

It returns zero if we take XOR of two same numbers.
It returns the same number if we XOR with zero.
So we can XOR all the numbers in the input; duplicate numbers will zero out each other 
and we will be left with the single number.
'''


arr = [1, 1, 3, 3, 5, 5, 7] #odd middle
arr = [1, 1, 2, 3, 3] #even in middle
arr = [1, 2, 2, 3, 3] #even in middle
arr = [1, 1, 3, 3, 5] #even in middle
arr = [1]
arr = [1, 1, 3, 3, 5, 7, 7] #odd
arr = [1, 1, 3, 3, 5, 5, 7, 7, 8] #odd
arr = [1, 1, 3, 3, 7, 7, 8, 9, 9]
arr = [1, 1, 2, 3, 3, 5, 5, 7, 7]
'''
time complexity : O(logN)
Space complexity O(1)
'''               
 def identify_outlier(arr):
    left = 0
    right = len(arr)-1
    
    while left < right:
        mid = left + (right-left)//2
        halves_are_even = (right - mid) % 2 ==0

        if arr[mid] == arr[mid+1]:
            if halves_are_even:
                left = mid +2

            else:
                
                right = mid -1
                
        elif arr[mid] == arr[mid-1]:
            if halves_are_even:
                right = mid-2
            else:
                left = mid+1
        else:
            return arr[mid]
    return arr[left] #edge case in the corner
            
  
                
print(identify_outlier(arr))      



