

'''
Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that 
should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''



    def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Write the elements of num2 into the end of nums1.
        for i in range(n):
            nums1[i + m] = nums2[i]
        # Sort nums1 list in-place.
        nums1.sort()   
        return nums1

nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3

merge([1,2,3,0,0,0], 3, [2,5,6],3)
merge([1], 1, [],0)
merge([0], 0, [1],1)
######################
def mergesort(nums1,m,nums2,n):
    #last index nums1
    last = m+n-1
    
    #merge in reverse order
    while m>0 and n>0:
        if nums1[m-1] > nums2[n-1]:
            nums1[last] = nums1[m-1]
            m-=1
        else: 
            nums1[last] = nums2[n-1]
            n-=1
        last-=1
    while n>0:
        nums1[last] = nums2[n-1]
        n, last = n-1, last-1
    return nums1
        
mergesort([1,2,3,0,0,0], 3, [2,5,6],3)    

######################

# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
  
# Code to print the list
  
  
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
  
# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
  
# This code is contributed by Mayank Khanna
