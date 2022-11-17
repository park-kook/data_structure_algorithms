
'''
Facebook onsite interview1
Problem
Given a list of integers and a target number, write a function that returns a boolean indicating 
if its possible to sum two integers from the list to reach the target number

Requirements
Try pen/paper before coding out your solution

You can not use an integer element twice. Optimize for time over space

Solution
For this problem we will take advantage of a set data structure. W
e will make a single pass through the list of integers, treating each element 
as the first integer of our possible sum.

At each iteration we will check to see if there is a second integer 
which will allow us hit the target number, adn we will use a set to check 
if we've already seen it in our list.

We will then update our seen set by adding the current number in the iteration to it.

Let's see this coded out:
'''


solution([1,3,5,1,7],4)

def twoSum(nums,target):
    h={}
    for i, num in enumerate(nums):
        n = target - num
        if n not in h:
            h[num]=i
        else: 
            return h[n],i      
twoSum([1,3,5,1,7],4)


            
            
            
def solution(lst,target):
    
    # Create set to keep track of duplicates
    seen = set()
    
    # We want to find if there is a num2 that sums with num to reach the target
    
    for num in lst:
        
        num2 = target - num
        
        if num2 in seen:
            return True
        else:
            seen.add(num)
        
    # If we never find a pair match which creates the sum
    return False

solution([1,3,5,1,7],4)
solution([1,3,5,1,7],14)
