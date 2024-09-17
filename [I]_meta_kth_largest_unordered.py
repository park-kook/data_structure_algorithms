'''
Problem Statement

Given an unordered array input = [3, 6, 2, 18, 29, 4, 5], find the  k -th largest element.

Let’s assume  k = 3  for this example. This means we want to find the 3rd largest element in the array.

'''

def kth_largest_sort(arr, k):
    # Sort the array in descending order
    arr_sorted = sorted(arr, reverse=True)
    # Return the k-th largest element
    return arr_sorted[k-1]

input_array = [3, 6, 2, 18, 29, 4, 5]
k = 3
result = kth_largest_sort(input_array, k)
result

'''
Time Complexity

	•	Sorting the array: The most time-consuming step is sorting the array, 
 which typically takes  O(N \log N)  time, where  N  is the number of elements in the array.
	•	Accessing the  k -th element: This is an  O(1)  operation.
'''


'''
Another optimized approach to find the  k -th largest element is 
by using the Quickselect algorithm. This algorithm is based on 
the same idea as the QuickSort algorithm but only partially sorts the array, 
making it more efficient for this problem.

Approach 3: Quickselect Algorithm

Quickselect is a selection algorithm to find the  k -th smallest (or largest)
element in an unordered list. It is related to the QuickSort sorting algorithm.
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
input_array = [3, 6, 2, 18, 29, 4, 5]
k = 3
result = kth_largest(input_array, k)
result


'''
Explanation

	•	quickselect function: It selects a pivot (in this case, the rightmost element) 
 and partitions the array such that elements less than or equal to the pivot are on the left, 
 and elements greater than the pivot are on the right.
	•	kth_largest function: Converts the  k -th largest element request into an index 
 and calls the quickselect function.

 	•	Time Complexity: Average case  O(N) , worst case  O(N^2)  (though this is rare).
	•	Space Complexity:  O(1)  as it’s an in-place algorithm.

Explanation

	•	Partitioning: Similar to the partition step in QuickSort. We choose a pivot 
 and rearrange the array such that elements less than the pivot come before it 
 and elements greater than the pivot come after it.
	•	Recursion: Depending on the position of the pivot, we either recursively search 
 in the left or right partition.

Time Complexity

	•	Average Case: The Quickselect algorithm has an average time complexity of  O(N) . 
 This is because each partitioning step reduces the problem size by half, similar to binary search.
	•	Worst Case: The worst-case time complexity is  O(N^2) , but this is rare and 
 can be mitigated by choosing a good pivot (randomized pivot selection helps).

Space Complexity

	•	In-place operation: The Quickselect algorithm uses  O(1)  extra space 
 since the partitioning is done in-place.

Overall Space Complexity:  O(1) 


QuickSort and QuickSelect are two algorithms related to array partitioning but serve different purposes.
Let’s break them down.

QuickSort

QuickSort is a divide-and-conquer sorting algorithm that efficiently sorts an array by partitioning 
it around a “pivot” element.

Steps of QuickSort:

	1.	Pick a Pivot: Choose an element from the array. This can be any element, but often the last, 
 first, or a random element is chosen.
	2.	Partition: Rearrange the elements in the array so that all elements smaller than the pivot are 
 on the left, and all elements greater than the pivot are on the right. The pivot is now in its 
 correct sorted position.
	3.	Recursion: Recursively apply QuickSort to the sub-arrays on the left and right of the pivot.

Time Complexity:

	•	Average Case:  O(N \log N) 
	•	Worst Case:  O(N^2)  (this happens when the pivot is always the smallest or largest element, 
 but using randomized or “median-of-three” pivot selection can help avoid this).

Space Complexity:

	•	In-Place Version:  O(\log N)  (due to the recursion stack)

Example:

Consider the array: [3, 6, 8, 10, 1, 2, 1]

	1.	Choose a pivot (say 10), then partition the array: [3, 6, 8, 1, 2, 1, 10].
	2.	Recursively apply QuickSort on the sub-arrays [3, 6, 8, 1, 2, 1] and [].

QuickSort Visual:

	1.	Pick a pivot.
	2.	Partition array around pivot.
	3.	Recursively sort sub-arrays.

QuickSelect

QuickSelect is an algorithm similar to QuickSort, but instead of fully sorting the array, 
it focuses on finding the  k -th smallest or largest element in an unsorted array.

Steps of QuickSelect:

	1.	Pick a Pivot: Just like in QuickSort, choose a pivot element.
	2.	Partition: Partition the array so that elements smaller than the pivot are on the left 
 and elements greater than the pivot are on the right.
	3.	Recurse on One Side: After partitioning, check the position of the pivot:
	•	If the pivot is at position  k , return it.
	•	If  k  is less than the pivot index, recurse on the left side.
	•	If  k  is greater, recurse on the right side.

Time Complexity:

	•	Average Case:  O(N)  because you are only sorting one partition at each step.
	•	Worst Case:  O(N^2) , but this can be rare if you use a randomized pivot selection.

Space Complexity:

	•	In-Place Version:  O(1) , with recursion stack  O(\log N) .

Example:

Find the 3rd largest element in [3, 6, 8, 10, 1, 2, 1]:

	1.	Pick a pivot, say 10. Partition the array: [3, 6, 8, 1, 2, 1, 10].
	2.	Since 10 is larger than the 3rd largest, recurse on the left sub-array [3, 6, 8, 1, 2, 1].
	3.	Continue partitioning until you find the 3rd largest.

QuickSelect Visual:

	1.	Pick a pivot.
	2.	Partition array around pivot.
	3.	Recurse on one partition to find the  k -th smallest or largest element.

Key Differences:

	•	QuickSort: Sorts the entire array.
	•	QuickSelect: Only partially sorts the array to find a specific element (like the  k -th largest 
 or smallest).

Both algorithms are widely used in practice due to their average-case efficiency and ease of 
implementation.

'''
