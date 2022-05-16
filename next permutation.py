 

    def nextPermutation(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        found = False
        i = len(nums)-2
        while i >=0:
            if nums[i] < nums[i+1]:
                found =True
                break
            i-=1
        if not found:
            nums.sort()
        else:
            m = findMaxIndex(i+1,nums,nums[i])
            nums[i],nums[m] = nums[m],nums[i]
            nums[i+1:] = nums[i+1:][::-1]
        return nums
    def findMaxIndex(index,a,curr):
        ans = -1
        index = 0
        for i in range(index,len(a)):
            if a[i]>curr:
                if ans == -1:
                    ans = curr
                    index = i
            else:
                ans = min(ans,a[i])
                index = i
        return index

nextPermutation([1,2,3])
nextPermutation([3,2,1])
nextPermutation([1,1,5])
nextPermutation([1])


nextPermutation([1,2,5,4,3]) #1,3,2,4,5


    def nextPermutation( nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
   # Get last ascending number from right - this is our pivot or boundary        
        i = len(nums)-1
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        
        # swap number just to left of pivot  with the first number from end of the array  that is greater than it
        if i != 0:
            j = len(nums)-1
            while j>0 and nums[j]<=nums[i-1]:
                j-=1
            nums[j],nums[i-1] = nums[i-1],nums[j]
        
        
       
        # reverse the array from i-len(nums)-1
        k = i
        m = len(nums)-1
        while k<m:
            nums[k],nums[m] = nums[m],nums[k]
            m-=1
            k+=1
        return nums
            
nextPermutation([1,2,3])
