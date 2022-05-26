'''
Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing) at least one number)
    which has the largest sum and return its sum

Time Complexity: O(N * log k) or O(n * k * log k), where, ‘N’ is the total number of elements among 
all the linked lists, ‘k’ is the total number of lists, and ‘n’ is the size of each linked list.
Insertion and deletion operation will be performed in min-heap for all N nodes.
Insertion and deletion in a min-heap require log k time.
Auxiliary Space: O(k).
The priority queue will have atmost ‘k’ number of elements at any point of time, hence 
the additional space required for our algorithm is O(k).    

'''

nums = [-2,1,-3,4,-1,2,1,-5,4]
output = 6 #4, -1, 2, 1
def maxSubarray(nums):
    maxSub = nums[0]
    curSum = 0
    
    for n in nums:
        if curSum <0:
            curSum = 0
        curSum +=n
        maxSub = max(maxSub, curSum)
    return maxSub
maxSubarray(nums)
