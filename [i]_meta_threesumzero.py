'''
#meta mock interview
'''
    def threeSum(nums):    
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
    # Now fix the first element
    # one by one and find the
    # other two elements
        N, result = len(nums), []
        for i in range(len(nums)):
            if nums[i] == nums[i-1]: # prevent from dulplicate set, shold not go through if previous value is the same
                continue 
            print(i)

            target = nums[i]*-1 #reduce to two sum proble, a+b = -c
            l= i+1 #index of the first element in the remining elements- not duplicate
            r =len(nums)-1 # index of the last element
            while l<r:
                if nums[l]+nums[r] == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l = l+1
                    while l<r and nums[l] == nums[r-1]:
                        l = l+1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return result
    

threeSum([-1,0])        
threeSum([-1,0,1,2,-1,-4])    
threeSum([-2,-2,0,0,2,2])  



def threesumzero(arr):
    arr.sort()
    if len(arr)<3:
        return print("None")

    for i in range(len(arr)-2):
        left = i+1
        right = len(arr)-1
        while left<right:
            if arr[i]+arr[left]+arr[right] ==0:
                print(arr[i],arr[left],arr[right])
                left+=1
                return 
            elif arr[i]+arr[left]+arr[right] <0:
                left+=1
            else:
                right-=1
    return print('Null')
                
threesumzero(arr)                
