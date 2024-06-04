'''
Given an array of N non-negative integers arr[] representing an elevation map 
where the width of each bar is 1, compute how much water it is able to trap after raining.
Time Complexity: O(N)
Auxiliary Space: O(1)
'''

def findWater(arr, n): 
  
    # left[i] contains height of tallest bar to the 
    # left of i'th bar including itself 
    left = [0]*n 
  
    # Right [i] contains height of tallest bar to 
    # the right of ith bar including itself 
    right = [0]*n 
  
    # Initialize result 
    water = 0
  
    # Fill left array 
    left[0] = arr[0] 
    for i in range(1, n): 
        left[i] = max(left[i-1], arr[i]) 
  
    # Fill right array 
    right[n-1] = arr[n-1] 
    for i in range(n-2, -1, -1): 
        right[i] = max(right[i + 1], arr[i]) 
  
    # Calculate the accumulated water element by element 
    # consider the amount of water on i'th bar, the 
    # amount of water accumulated on this particular 
    # bar will be equal to min(left[i], right[i]) - arr[i] . 
    for i in range(0, n): 
        water += min(left[i], right[i]) - arr[i] 
  
    return water 
  
  
# Driver program 
if __name__ == '__main__': 
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] 
    n = len(arr) 
    print(findWater(arr, n)) 
#output =6


def maxWater(arr, n): 
      
    # Indices to traverse the array 
    left = 0
    right = n-1
  
    # To store Left max and right max  
    # for two pointers left and right 
    l_max = 0
    r_max = 0
  
    # To store the total amount  
    # of rain water trapped 
    result = 0
    while (left <= right): 
          
        # We need check for minimum of left  
        # and right max for each element 
        if r_max <= l_max: 
              
            # Add the difference between  
            #current value and right max at index r 
            result += max(0, r_max-arr[right]) 
              
            # Update right max 
            r_max = max(r_max, arr[right]) 
              
            # Update right pointer 
            right -= 1
        else: 
              
            # Add the difference between  
            # current value and left max at index l 
            result += max(0, l_max-arr[left]) 
              
            # Update left max 
            l_max = max(l_max, arr[left]) 
              
            # Update left pointer 
            left += 1
    return result 
  
  
# Driver code 
if __name__ == '__main__': 
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] 
    N = len(arr) 
    print(maxWater(arr, N)) 
  
# This code is contributed by Nikhil Chatragadda 
