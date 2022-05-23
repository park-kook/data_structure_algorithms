'''
longest increasing subsequence
given an integer array nums, return the length of the longest strictly increasing subsequence

A subsequence is a sequence that can be derived from an array by deleting some or no elments 
without changing the order of the remaining elements. e.g. [3,6,2,7] is a subsequence of the array 
[0,3,1,6,2,2,7]
O(N^2) - Dynamic programming

at last node, there is no further continous, so it is alwasy one count so we need to reverse from bottom up
of dynamic programming
'''
nums = [10,9,2,5,3,7,101,18]
output = 4 #[2,3,7,101]

nums = [0,1,0,3,2,3]
output = 4 #[0,1,2,3]

def lengthOfLIS(nums):
    LIS = [1]*len(nums) #at last node, there is no further continous, 
    #so it is alwasy one count so we need to reverse from bottom up of dynamic programming
    
    for i in range(len(nums)-1, -1, -1):

        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i],1+LIS[j])
    return max(LIS)
lengthOfLIS(nums)
