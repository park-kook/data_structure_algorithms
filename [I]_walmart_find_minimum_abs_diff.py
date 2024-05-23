'''
Given two arrays , find the minimum absolute difference pair of numbers . 

Pair :  one number picked from each array. 
[10, 28,30] 

[22, 19, 35,60] 

Pair : (30,35) , Min absolute difference : 5 

---------------------------- 

1) No code execution needed 

2) Time complexity 

3) Test cases tracing  

4) Coding standards  


--------------------------- 


'''
arr1 = [1,3,5]
arr2 = [6,7,8]

arr1.sort()
arr2.sort()
min_diff = float('inf')
left1, left2 = 0,0
while left1 < len(arr1) and left2 < len(arr2):
  diff = abs(arr1[left1] - arr2[left2])
  if diff < min_diff:
    pair = (arr1[left1],arr2[left2])
  min_diff = min(diff, min_diff)

if arr1[left1] < arr2[left2]:
  left1+=1
else:
  left2+=1

min_diff,pair
