'''
Homedepot interview
# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
'''
def union(arr1, arr2):
    res=set()
    for i in arr1:
        res.add(i)
    for i in arr2:
        res.add(i)
    return res
union(arr1, arr2)    

def printIntersection(arr1, arr2):
    hs = set()
    n1 = len(arr1)
    n2 = len(arr2)
 
    # Insert the elements of arr1[] to set S
    for i in range(0, n1):
        hs.add(arr1[i])
#    print("Intersection:")
    for i in range(0, n2):
 
        # If element is present in set then
        # push it to vector V
        if arr2[i] in hs:
            
            print(arr2[i], end=" ")

arr1 = [4,9,5]
arr2 = [9,4,9,8,4]

printIntersection(arr1, arr2)
# Write a function that prints a dictionary where keys are between 1 and 20 and their corresponding values are the square of the keys
def dictionary():
    a={}
    
    for x in range(20):
        a[x] = x^2
    print(a)
#    return a

dictionary()
#    A={}
    A = {x: x^2 for x in range(20)}
    print(A)
    
dict2()

# Output all numbers between 0 and 100 that are divisible by 2 and 5, using list comprehension.

[x for x in range(100) if x%5==0 and x%2==0]

[x if x%5==0 and x%2==0 else None for x in range(100)]
#[x if x%5==0 and x%2==0 for x in range(100)]
i=4
def intersection(arr1, arr2):
    
    dict_1 = {}
    dict_2 = {}
    
    res = ""
#    res = []
    for i in arr1:
        dict_1[i] = 1+dict_1.get(i,0)
    for i in arr2:
        dict_2[i] = 1+dict_1.get(i,0)
            
#    i = 4        
    for i in dict_1:

        if i in dict_2:

            res+=(str(i)*int(min(dict_1[i], dict_2[i]))) #"4499'
#            ','.join(res)
#            res.append(str(i)*int(min(dict_1[i], dict_2[i])/min(dict_1[i], dict_2[i])))  
#            res.append(str(i)*int(min(dict_1[i], dict_2[i]))) 
            res = [int(i) for i in res]
    return res

intersection(arr1, arr2)
