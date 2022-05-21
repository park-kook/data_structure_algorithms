
'''
Longest Consecutive Squence 
Given an unsorted array of integers, find the length of the longest consecutive element sequence
your algorithm should run in O(n) complexity

count if there is previous number or not of the number in the loop

'''
nums = [100,4,200,1,3,2]
output: 4

def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0
    
    for n in nums:
        #check if its the start of a sequence
        if (n-1) not in numSet:
            length = 0
            while (n+length) in numSet:
                length +=1
            longest = max(length, longest)
        
    return longest

longestConsecutive(nums)
