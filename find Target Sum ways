''' XXXX don't understand yet XXXXXXX
dynamic programming
you are given an integer array nums and an integer target.  
By adding one of the symbol + and - before each integer 
in nums and then concatenate all the integers. 
input: nums=[1,1,1,1,1], target = 3
output:5 there are 5 ways to assign symbols to make the sum of nums to be target 3. 


'''

nums=[1,1,1]
target=1
def findTargetSumWays(nums,target):
    dp={}
    
    
    def backtrack(index, total):
        if index==len(nums): #base case
            return 1 if total == target else 0
        
        if (index,total) in dp:
            return dp[(index,total)]
        dp[(index,total)] = (backtrack(index + 1, total + nums[index]) + 
                              backtrack(index +1, total - nums[index]))
        return dp[(index, total)]
    return backtrack(0,0)
    
findTargetSumWays(nums,target)  
