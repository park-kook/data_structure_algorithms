
equilibrium3(nums)

'''
Equilibirum index: An index of an array such that the sum of elements at lower indexes is equal to
the sum of elements at higher indexes
# 3 is an equilibrium index, because:
# A[0] + A[1] + A[2]  =  A[4] + A[5] + A[6]
'''
nums = [-7,1,5,2,-4,3,0] 
#sum - i1-i2-i3
output = 3
nums = [0,1,5,2,-4,-3,-1]

nums = [0,1,5,2,-4,-3,-1]
def equilibrium(nums):
    l_sum, r_sum = 0,0
#    length = len(nums)

    for i in range(len(nums)):
        l_sum = 0
        r_sum = 0
        
        for l in range(i): #left sum

            l_sum+= nums[l]
        for r in range(i+1, len(nums)): #right sum

            r_sum+= nums[r]
            
        if l_sum == r_sum:
            return i
    return -1

equilibrium(nums)

nums = [-7, 1,5,2, -4, 3, 0]
def equalibrium(nums):
    total_sum = sum(nums)
    left_sum = 0
    output = []
    for i in range(1, len(nums)):
        left_sum += nums[i-1]
        right_sum = total_sum-left_sum-nums[i]
        if left_sum == right_sum:
            output.append(i)
            #return i
    #return -1
    return output


nums = [0,1,5,2,-4,-3,-1] #sum = 0

nums = [-7,1,5,2,-4,3,0] #sum = 0
def equilibrium3(nums):
    l_sum = 0
#    length = len(nums)
    total_sum = sum(nums) # #um = 0
    for i in range(len(nums)):

        total_sum-=nums[i] #right sum

        if total_sum == l_sum:
            return i
        
        l_sum+= nums[i] #left sum
    return -1
 
equilibrium3(nums)
nums = [0,1,5,2,-4,-3,-1] #sum = 0







def pivotIndex(nums):
    left = 0
    pivot = 0
    right = sum(nums)-nums[0]
    while pivot < len(nums)-1 and right != left:
        pivot += 1
        right -= nums[pivot]
        left += nums[pivot-1]
 
    return pivot if left == right else -1


pivotIndex(nums)
