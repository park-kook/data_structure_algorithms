

'''
Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order 
of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
'''
    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        
        for i in range(len(nums)):

            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        return nums
                
                
moveZeroes([0,1,0,3,12])  
moveZeroes([1,0,0,3,12])             
                
    def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        append_times=nums.count(0)
        for i in range(append_times):
            nums.remove(0) #  Delete the front zero
            nums.append(0) # append it at the end of nums, the times of the addition and substraction shall be equal
        return nums

moveZeroes([0,1,0,3,12])  
moveZeroes([1,0,0,3,12])  

nums=[0,1,0,3,12]
nums.count(0)
