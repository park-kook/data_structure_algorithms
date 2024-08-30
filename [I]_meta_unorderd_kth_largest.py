'''
unordered array with N values input = [3,6,2,18,29,4,5] 
implement a fuundion that finds the kth largest value in the array and the return value
'''

def quickselect(arr, left, right, k):
    pivot = arr[right]
    partition_index = left
    
    for i in range(left, right):
        if arr[i] <= pivot:
            arr[i], arr[partition_index] = arr[partition_index], arr[i]
            partition_index += 1
    
    arr[partition_index], arr[right] = arr[right], arr[partition_index]
    
    if partition_index == k:
        return arr[partition_index]
    elif partition_index < k:
        return quickselect(arr, partition_index + 1, right, k)
    else:
        return quickselect(arr, left, partition_index - 1, k)

def kth_largest(arr, k):
    return quickselect(arr, 0, len(arr) - 1, len(arr) - k)

# Example usage
input_array = [3, 6, 2, 18, 29, 4, 5] #[5,6,2,18,29,4,3]
k = 2
result = kth_largest(input_array, k)
result
