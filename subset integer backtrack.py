
backtrack problem
Given an integer array nums, retuan all possible subsets   (The power set)
the solution set must not contain duplciate subsets.
of note this is not permutation so this does not include duplicate
down node has two options (emptry and adding in)
'''
input: nums = [1,2,3]
output= [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#2**3 = number of subsets
nums = [1,2,3]
def subsets(nums):
    res=[] #global outside of sub function
    
    subset = [] #global outside of sub function
    def dfs(i):
        if i>=len(nums):
            res.append(subset.copy())
            return
        
        #decision to include nums[i]
        subset.append(nums[i])
        dfs(i+1)
        
        #decision Not to include nums[i]
        subset.pop()
        dfs(i+1)
        
    dfs(0)
    return res

subsets(nums)

output = [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
