'''
three sum questions
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

'''
def threeSum(nums):
    res = []
    nums.sort()
    
    for i, a in enumerate(nums):
        if i>0 and a==nums[i-1]:
            continue
        l,r = i+1, len(nums)-1
        while l<r:
            threeSum = a + nums[l]+ nums[r]
            if threeSum >0:
                r-=1
            elif threeSum <0:
                l+=1
            else: 
                res.append([a,nums[l],nums[r]])
                l+=1
                while nums[l]== nums[l-1] and l<r:
                    l+=1
    return res
threeSum([-4,-1,-1,0,1,2])
threeSum([-2,-2,0,0,2,2])  



#class Solution(object):
   # def threeSum(self, nums):
    def threeSum(nums):    
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        N, result = len(nums), []
        for i in range(N):
            if i > 0 and nums[i] == nums[i-1]:
                continue  #rejects all the remaining statments in the current iteration of the lopp, 
                #and moves the control back to the top of the loop
            target = nums[i]*-1 #reduce to two sum proble, a+b = -c
            s,e = i+1, N-1
            while s<e:
                if nums[s]+nums[e] == target:
                    result.append([nums[i], nums[s], nums[e]])
                    s = s+1
                    while s<e and nums[s] == nums[s-1]:
                        s = s+1
                elif nums[s] + nums[e] < target:
                    s = s+1
                else:
                    e = e-1
        return result
    

        
threeSum([-1,0,1,2,-1,-4])    
