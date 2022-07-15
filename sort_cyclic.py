'''
We are given an array containing n objects. Each object, 
when created, was assigned a unique number from the range 1 to n 
based on their creation sequence. This means that the object with sequence number 
3 was created just before the object with sequence number 4.

Write a function to sort the objects in-place on their creation sequence number in O(n)
and without using any extra space. 
'''
nums = [3, 1, 5, 4, 2] #->5,1,3,4,2->4,1,3,5,2 ->3,1,4,5,2->2,1,4,5,3->1,2,4,5,3->1,2,5,4,3->1,2,3,4,5
output = [1,2,3,4,5]

def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i]-1
        if nums[i] != nums[j]:
            nums[i],nums[j] = nums[j],nums[i]
        else: 
            i+=1
    return nums
cyclic_sort(nums)        
