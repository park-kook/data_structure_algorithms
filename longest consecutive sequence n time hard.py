
'''
Longest Consecutive Squence 
Given an unsorted array of integers, find the length of the longest consecutive element sequence
your algorithm should run in O(n) complexity
space complexity O(1)

count if there is previous number (n-1) or not of the number in the loop

100, 4, 200, 1, 3, 2
starting from 1 above and adding length 1 more until n+lengh in numSet:
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



'''
another version
time complexity nlog(n)
space complexity o(n)
Complexity Analysis: 

Time complexity: O(nLogn). 
Time to sort the array is O(nlogn).
Auxiliary space : O(1). 
As no extra space is needed.

'''

# Python3 program to find longest
# contiguous subsequence
 
# Returns length of the longest
# contiguous subsequence
def findLongestConseqSubseq(arr, n):
     
    ans = 0
    count = 0
 
    # Sort the array
    arr.sort()
 
    v = []
 
    v.append(arr[0])
 
    # Insert repeated elements only
    # once in the vector
    for i in range(1, n):
        if (arr[i] != arr[i - 1]):
            v.append(arr[i])
 
    # Find the maximum length
    # by traversing the array
    for i in range(len(v)):
 
        # Check if the current element is
        # equal to previous element +1
        if (i > 0 and v[i] == v[i - 1] + 1):
            count += 1
             
        # Reset the count
        else:
            count = 1
             
        # Update the maximum
        ans = max(ans, count)
         
    return ans
 
# Driver code
arr = [ 1, 2, 2, 3 ]
n = len(arr)
 
print("Length of the Longest contiguous subsequence is",
       findLongestConseqSubseq(arr, n))
 
# This code is contributed by avanitrachhadiya2155
