
'''
Kth largest Element in an array
Given an integer array nums and an integer k, return the k th largest element in the array. 
Note that it is the k th largest element in the sorted order, not the kth distinct element

'''
nums =[3,2,1,5,6,4]
k=2
output = 5


nums = [3,2,3,1,2,4,5,5,6]
k=4
output= 4

def findKthLargest(nums, k):
    nums.sort()
    return nums[len(nums)-k]

def findKthLargest(nums,k):
    k = len(nums)-k
    
    def quickSelect(l,r):
        left_p, r_pivot = l, nums[r]
        
        for i in range(l,r):
            if nums[i] <= r_pivot:
#                nums[left_p], nums[i] = nums[i], nums[left_p]
                left_p+=1
        nums[left_p], nums[r] = nums[r], nums[left_p]
        
        if left_p>k: return quickSelect(l,left_p-1)
        elif left_p<k: return quickSelect(left_p+1,r)
        else: return nums[left_p]
    return quickSelect(0, len(nums)-1)

findKthLargest(nums,k)
k = 6-2 = 4
4
3, 2, 1, 
4,6,5
p+1 = 4 = l = p
r = 5
nums=[6,5]
l = 6 =  p
r = 5  =pivot
nums=[5,6]

8 = pivot = r = num[8]
k = 9-4 = 5
p = 0 = l
[3,2,3,1,2,4,5,5,6]
pivot = 6
p = 8

p-1 = 7 = r
l = 0
[3,2,3,1,2,4,5,5]
p=7
p-1 = 6 = r
l = 0
[3,2,3,1,2,4,5]
 
p=6-1
p=5
l = 0
[3,2,3,1,2,4]

for i in range(0,6):
    print(i)
