
##################################
'''
132 pattern, given array of n integers nums, a 132 pattern is a subsequence of three integers nums[i],nums[j] and
nums[k] such that i<j<k and nums[i]<nums[k]<nums[j]
Return True if there is 132 patter in nums, otherwise, return False
'''
nums=[3,1,4,2]
def find132pattern(nums):
    stack = [] #mono decreasing
    curMin = nums[0]
    
    for n in nums[1:]:
        while stack and n>=stack[-1][0]:
            stack.pop()
        if stack and n>stack[-1][1]:
            return True
        stack.append([n,curMin])
#        curMin = min(curMin,n)
        if curMin > n:
            curMin = n
    return False

nums=[5,3,1,4,2]
find132pattern(nums)
stack.append([3,5])
stack.append([1,3])
stack.pop()
stack.pop()
stack.append([4,1])

nums=[3,4,4,2,4,3]
stack = []
stack.append([4,3]) #1
stack.pop()
stack.append([4,3]) #2
stack.append([2,3]) #3
stack.pop()
stack.pop()
stack.append([4,2]) #4

stack[2][0]
