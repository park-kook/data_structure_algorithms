'''
Here’s a Python function that rearranges the elements 
in the array so that all nonzero elements are moved 
to the left, and zeros are moved to the right. 
The function also returns the number of nonzero elements.

Python Code:
'''
def move_nonzero_left(arr):
    # Pointer to place the next nonzero element
    last_nonzero_index = 0
    
    # Traverse the array
    for i in range(len(arr)):
        if arr[i] != 0:
            # Swap the current nonzero element with the element at last_nonzero_index
            arr[i], arr[last_nonzero_index] = arr[last_nonzero_index], arr[i]
            last_nonzero_index += 1
    
    # The number of nonzero elements is equal to last_nonzero_index
    return arr, last_nonzero_index

# Example usage:
arr = [1, 0, 2, 0, 3, 4]
result, nonzero_count = move_nonzero_left(arr)
print(f"Rearranged Array: {result}")
print(f"Number of Nonzero Elements: {nonzero_count}")

'''
Example Output:

Rearranged Array: [1, 2, 3, 4, 0, 0]
Number of Nonzero Elements: 4

Explanation:

	1.	Pointer Initialization: We initialize a pointer last_nonzero_index to keep track of where the next nonzero element should be placed.
	2.	Iteration: We iterate through the array. Each time we encounter a nonzero element, we swap it with the element at last_nonzero_index and increment last_nonzero_index.
	3.	Count: The value of last_nonzero_index at the end of the loop gives us the count of nonzero elements.

Time Complexity:

	•	O(n): The function traverses the array once, so the time complexity is linear with respect to the size of the input array.

Space Complexity:

	•	O(1): The function uses only a constant amount of extra space (a few variables), so the space complexity is constant. The array is modified in place.

This code efficiently brings all nonzero elements to the left side of the array, followed by zeros, and returns the count of nonzero elements.

'''