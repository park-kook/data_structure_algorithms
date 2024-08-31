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
    print(i)
    print(partition_index)
    print(arr)
    if partition_index == k:
        return arr[partition_index]
    elif partition_index < k:
        return quickselect(arr, partition_index + 1, right, k)
    else:
        return quickselect(arr, left, partition_index - 1, k)

def kth_largest(arr, k):
    return quickselect(arr, 0, len(arr) - 1, len(arr) - k)

# Example usage
# Example usage
input_array = [3, 6, 2, 18, 29, 4, 5] #[3,2,6,18,29,4,5], [3,2,4,18,29,6,5], [3,2,4,5,29,6,18], index = 3, 
#[3,2,4,5,6,29,18], indedx = 5, 
k = 2 # k=5 (len(input_array) - k) 
result = kth_largest(input_array, k)
result


'''
5
3
[3, 2, 4, 5, 29, 6, 18]
5
5
[3, 2, 4, 5, 6, 18, 29]
'''
