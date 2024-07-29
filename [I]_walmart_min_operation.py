'''
Minimum Operations to Reduce X to Zero

You are given an integer array nums and an integer x. 
In one operation, you can either remove the leftmost or the rightmost 
element from the array nums and subtract its value from x. 
Note that this modifies the array for future operations. Return the minimum 
number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
'''


def min_operations(nums, x):
    target = sum(nums) - x
    if target == 0:
        return len(nums)
    n = len(nums)
    left = 0
    current_sum = 0
    max_len = -1
    for right in range(n):
        current_sum += nums[right]
        while current_sum > target and left <= right:
            current_sum -= nums[left]
            left += 1
        if current_sum == target:
            max_len = max(max_len, right - left + 1)
    return n - max_len if max_len != -1 else -1

# Example usage:
nums = [1, 1, 4, 2, 3]
x = 5
print(min_operations(nums, x))  # Output: 2
