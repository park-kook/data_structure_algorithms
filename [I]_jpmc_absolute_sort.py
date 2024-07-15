'''
Time Complexity
Average Case: 

O(nlogn)
Worst Case: 
O(n 2 ) (occurs when the pivot selection is poor, e.g., always choosing the smallest or largest element in a sorted or reverse-sorted array)
Space Complexity
Average Case: 

O(logn) due to recursive calls
Worst Case: 

O(n) in the worst-case recursion depth
'''

def absolute_quick_sort(arr):
    # Helper function to get the absolute value
    def absolute_value(x):
        return x if x >= 0 else -x

    # QuickSort function
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if absolute_value(x) < absolute_value(pivot)]
            middle = [x for x in arr if absolute_value(x) == absolute_value(pivot)]
            right = [x for x in arr if absolute_value(x) > absolute_value(pivot)]
            return quick_sort(left) + middle + quick_sort(right)

    return quick_sort(arr)

# Example usage
array = [-5, -1, 2, -10, 3]
sorted_array = absolute_quick_sort(array)
print("Original array:", array)
print("Sorted array by absolute values:", sorted_array)
