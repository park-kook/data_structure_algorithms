'''
Given an array nums, a peak element is one that is greater than its neighbors. 
Write a function that returns the index of any peak element. It is guaranteed that such a peak exists.
'''

Input:  nums = [5, 4, 6, 1, 2, 4, 1]


def find_peak(nums):
    """
    Finds any peak element index in the array.
    
    A peak is an element that is strictly greater than its neighbors.
    We use binary search to achieve O(log n) time complexity.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2

        # Line-by-line explanation:

        # ✅ If the middle element is greater than its next, we may be on the descending slope
        # So, the peak is on the left half (could be mid itself)
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            # ✅ Else, we're on the ascending slope, so the peak must be on the right side
            left = mid + 1

    # ✅ When left == right, we found a peak
    return left




'''
🧠 Explanation:

We use a binary search strategy instead of scanning the whole array:
	•	At every step, we check nums[mid] and nums[mid+1].
	•	If nums[mid] > nums[mid+1], the peak might be on the left (including mid), so right = mid.
	•	Else, the peak must be on the right, so left = mid + 1.

This works because there must be a peak due to how the array “changes direction” — if it’s going up, it must come down somewhere.

⸻

📈 Time and Space Complexity:
	•	Time: O(log n) — because we halve the search space each iteration.
	•	Space: O(1) — we only use a few pointers, no extra arrays.
'''


# Version 2: Linear Scan (Brute-force)


def find_peak_linear(nums):
    """
    Finds any peak element index in the array by linear scan.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(nums)

    for i in range(n):
        # First element case
        if i == 0:
            if n == 1 or nums[i] > nums[i + 1]:
                return i

        # Last element case
        elif i == n - 1:
            if nums[i] > nums[i - 1]:
                return i

        # Middle elements
        elif nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i

    return -1  # fallback (should never happen if at least one peak exists)
