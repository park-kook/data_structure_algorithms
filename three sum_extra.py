
'''
Given an array of integers that is already sorted in ascending order. Find
two numbers such that they add up to a specific target number. 
The function twoSum should return indices of the two numbers such that they add up to that target,
where index1 must be less than index2
Time Complexity: O(N).
Space Complexity: O(1).
'''
numbers = [2,8,11,15]
numbers = [2,15,8,11]
target = 10

def twoSum(numbers, target):
    l,r = 0, len(numbers)-1
    while l<r:
        curSum = numbers[l] + numbers[r]
        
        if curSum > target:
            r-=1
        elif curSum < target:
            l+=1
        else:
            return [l, r]
    return -1


twoSum(numbers, target)


def twosum(nums, target):
    d={}
    for i, v in enumerate(nums):
        if target-v not in d:
            d[v] = i
        else: 
            return d[target-v],i
nums = [2,8,11,15]
nums = [2,15,11,8]
target = 10   
twosum(nums, target)        


'''
educative four sum
Quadruple Sum to Target (medium)#
Given an array of unsorted numbers and a target number, 
find all unique quadruplets in it, whose sum is equal to the target number.
Time complexity#
Sorting the array will take O(N∗logN). Overall searchQuadruplets() will take O(N∗logN+N^3)
, which is asymptotically equivalent to O(N^3).

Space complexity#
The space complexity of the above algorithm will be O(N), which is required for sorting.
'''
arr = [4, 1, 2, -1, 1, -3] #[-3, -1, 1, 1, 2, 4]
target=1
output = [-3, -1, 1, 4], [-3, 1, 1, 2]

arr =[2, 0, -1, 1, -2, 2] #[-2, -1, 0, 1, 2, 2]
target=2
Output = [-2, 0, 2, 2], [-1, 0, 1, 2]

def search_quadruplets(arr, target):
  quadruplets = []
  arr.sort() 
  # TODO: Write your code here
  for i in range(len(arr)):
    if arr[i] == arr[i-1]:
      continue      
#    print(arr[i])
    for j in range(i+1, len(arr)):
      if arr[j] == arr[j-1]:
        continue
        
      left = j+1
      right = len(arr)-1

      while left < right:
        total = target - (arr[i]+arr[j]+arr[left]+arr[right])
        if total > 0: 
          left+=1
#          right-=1          
        elif total <0:
          right-=1
#          left+=1
        else:
          quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
          left+=1
          right-=1
          if arr[left] == arr[left-1]:
              left+=1

  return quadruplets

search_quadruplets(arr, target)

educative three sum


arr = [-5, 2, -1, -2, 3]
arr.sort() #[-5, -2, -1, 2, 3]
output = [[-5, 2, 3], [-2, -1, 3]]
arr = [-3, 0, 1, 2, -1, 1, -2]
arr.sort() #[-3, -2, -1, 0, 1, 1, 2]
output  = [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]

'''
Given an array of unsorted numbers and a target number, 
find a triplet in the array whose sum is as close to the target number as possible, 
return the sum of the triplet. If there are more than one such triplet, 
return the sum of the triplet with the smallest sum.
'''
arr = [-2, 0, 1, 2] 
target_sum=2
output= 1 #[-2,1,2]

arr = [-3, -1, 1, 2]
target_sum=1
output= 0 #[-3,1,2]


arr = [1, 0, 1, 1]
target_sum=100
output= 3 #[1,1,1]

import math
num=0
left=1
right = 3

def triplet_sum_close_to_target(arr, target_sum):
  # TODO: Write your code here
  min_num = math.inf
  arr.sort()
  for num in range(len(arr)-2):
    left = num+1
    right = len(arr)-1
    while left < right: 
      total = arr[num] + arr[left] + arr[right]
      diff = target_sum - total
      if diff ==0:
          return total
      if abs(diff) < abs(min_num) or (abs(diff)==abs(min_num) and diff>min_num): #this is the key
          min_num = diff

      if total > 0:
        right-=1
      else:

        left+=1


  return target_sum - min_num
triplet_sum_close_to_target(arr, target_sum)
'''
Given an array arr of unsorted numbers and a target sum, 
count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, 
and k are three different indices. Write a function to return the count of such triplets.
'''
arr = [-1, 0, 2, 3]
target=3
output = 2
arr =[-1, 4, 2, 1, 3]
arr.sort() #[-1, 1, 2, 3, 4]
target=5
output = 4


num=0
left=1
right=4

def triplet_with_smaller_sum(arr, target):
  count = 0
  arr.sort()
  # TODO: Write your code here
  for num in range(len(arr)):
    left = num+1
    right = len(arr)-1
    while left < right:
      diff = target - (arr[num] + arr[left] + arr[right])
      if diff > 0:
        count+=1
#        print(arr[num] , arr[left] , arr[right])
        left+=1
      else:
        right-=1

  return count
triplet_with_smaller_sum(arr, target)



def triplet_with_smaller_sum(arr, target):
  count = 0
  arr.sort()
  # TODO: Write your code here
  for num in range(len(arr)):
    left = num+1
    right = len(arr)-1
    while left < right:
      total = arr[num] + arr[left] + arr[right]
      if target > total:
        count+=1

      if total>0:
        right-=1
      else:
        left+=1

  return count
triplet_with_smaller_sum(arr, target)


'''
Given an array with positive numbers and a positive target number, 
find all of its contiguous subarrays whose product is less than the target number.
'''
def find_subarrays(arr, target):
  result = []
  # TODO: Write your code here
  for i in range(len(arr)):
    left = i+1
    right = len(arr)-1
    if arr[i] < target:
      result.append([arr[i]])
    while left < right:
        if arr[left]<target:
            result.append([arr[left]])
        if int(arr[i] * arr[left]) < target:
            result.append([arr[i],arr[left]])
            left+=1
  return result
right = 0
right = 2
from collections import deque
def find_subarrays(arr, target):
  result = []
  product = 1
  left = 0
  for right in range(len(arr)):
    product *= arr[right]
    while (product >= target and left <= right):
      product /= arr[left]
      left += 1
    # since the product of all numbers from left to right is less than the target therefore,
    # all subarrays from left to right will have a product less than the target too; to avoid
    # duplicates, we will start with a subarray containing only arr[right] and then extend it
    temp_list = deque()
    for i in range(right, left-1, -1):
        print(i)
        temp_list.appendleft(arr[i])
        result.append(list(temp_list))
  return result

arr = [2, 5, 3, 10]
target = 30
output = [[2], [5], [2, 5], [3], [5, 3], [10]]
find_subarrays(arr, target)

Out[84]: [2, [2, 5], [2, 3], 5, [5, 3], 3, 10]
'''
three sum questions
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
the solution set must not contain duplicate triplets. 
'''
def search_triplets(arr):
  triplets = []
  arr.sort()
  # TODO: Write your code here
  for num in range(len(arr)-2):
    left = num+1
    right = len(arr)-1

    while left < right:
        total = arr[num] + arr[left] + arr[right]
        if total > 0:
            right-=1
        elif total<0:
            left+=1
        else:
            if arr[left] == arr[left-1]:
                left+=1  
            else: 
                triplets.append([arr[num], arr[left], arr[right]])
                left+=1   
        
  return triplets

search_triplets(arr)


 

#class Solution(object):
   # def threeSum(self, nums):
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
nums = [-4,-1,-1,0,1,2]         
nums[-1]
threeSum(nums)
nums = [-1,0,1,2,-1,-4]




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

threeSum([0,1,1,2,2,3])

threeSum([-4,-1,-1,0,1,2])


threeSum([-2,-2,0,0,2,2])  

arr = [0,1,-1,2,-2]
arr = [0,1]
arr = [-4,-1,-1,0,1,2]
arr = [-2,-2,0,0,2,2]

def threeSumZero(arr):
    if len(arr)<3:
#        print("None")
        return False
    res=[]
    arr.sort()
    
    for i in range(len(arr)-2):
        if arr[i] == arr[i-1]:
            continue
        left = i+1
        right = len(arr)-1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == 0:
#                print(arr[i], arr[left], arr[right])
                res.append([arr[i], arr[left], arr[right]])
                left+=1     
                while left <right and arr[left] ==arr[left-1]:
                    left+=1     
                    

#                return (arr[i], arr[left], arr[right])
                
            elif total < 0:
                left+=1
            else:
                right-=1
                
#    print("None")
    return res
arr = [-4,-1,-1,0,1,2]
arr = [-2,-2,0,0,2,2]
threeSumZero(arr)

'''
#meta mock interview
'''

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
