
'''
Minimum Window Sort (medium)#
Given an array, find the length of the smallest 
subarray in it which when sorted will sort the whole array.
'''
arr = [1, 2, 5, 3, 7, 10, 9, 12]
output = 5 #[5, 3, 7, 10, 9]
arr = [1, 3, 2, 0, -1, 7, 10] #low: 1 and high: 4
output = 5 #[1, 3, 2, 0, -1]

arr = [1, 2, 3]
output =0

arr = [3,2,1]
output = 3

def shortest_window_sort(arr):
    low = 0
    high = len(arr)-1
    while low < len(arr)-1 and arr[low]<=arr[low+1]:
        low+=1
    if low == len(arr)-1:
        return 0
    
    while high > 0 and arr[high] >= arr[high-1]:
        high-=1
        
        
    subarray_max = min(arr)
    subarray_min = max(arr)
    
    for k in range(low, high+1):
        subarray_max = max(subarray_max, arr[k]) #3
        subarray_min = min(subarray_min, arr[k]) #-1
        
    while low>0 and arr[low-1]>subarray_min:  
        low-=1
    while high< len(arr)-1 and arr[high+1]<subarray_max:
        high+=1
    return high-low +1
shortest_window_sort(arr)    
