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

            res+=(str(i)*int(min(dict_1[i], dict_2[i]))) #"94'
#            ','.join(res)
#            res.append(str(i)*int(min(dict_1[i], dict_2[i])/min(dict_1[i], dict_2[i])))  
#            res.append(str(i)*int(min(dict_1[i], dict_2[i]))) 
            res = [int(i) for i in res]
            #[9,4]
    return res

intersection(arr1, arr2)






a=[1,2]
b=a
b[1] = -2
a[1]+b[1]
#=-4


a=[1,2]
b=a.copy()
b[1] = -2
a[1]+b[1]
#=0 

a=(1,2)
a[1]=0
T#ypeError: 'tuple' object does not support item assignment

# Time Allowed: ~30 Minutes 

### SQL (1 Question) ###

# Show total cost for each business, sorted from cost highest to lowest.

# Table Business:
# +--------------+------+
# | BusinessName | Cost |
# +--------------+------+
# | Pear         |  100 |
# +--------------+------+
# | Pear         |  175 |
# +--------------+------+
# | Marketplace  |  220 |
# +--------------+------+
# | Horizon      |   50 |
# +--------------+------+
# | Marketplace  |  145 |
# +--------------+------+

# Expected Output:
# +--------------+------+
# | BusinessName | Cost |
# +--------------+------+
# | Marketplace  |  365 |
# +--------------+------+
# | Pear         |  275 |
# +--------------+------+
# | Horizon      |   50 |
# +--------------+------+

Select businessName, sum(cost) as sum_cost
From business
Group by businessName
Order by sum(cost) desc



### Python (3 Questions) ###


###### Q1 ######
# Write a function that prints a dictionary where keys are between 1 and 20 and their corresponding values are the square of the keys

Def dict():
    A={}
    for i in range(1,21):
        A[i] = i**2
    return A
dict()

#A = {x: x**2 for x in range(20)}

---

###### Q2 ######
# Output all numbers between 0 and 100 that are divisible by 2 and 5, using list comprehension.

Def all():
    res=[]
    For i in range(100):
        If i%2==0 and i%5 ==0:
        res.append(i)
    Return res
    
    
    
a = [x for x in range(10)]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = {x:None for x in range(10) }
'''
{0: None,
 1: None,
 2: None,
 3: None,
 4: None,
 5: None,
 6: None,
 7: None,
 8: None,
 9: None}
'''

[x for x in range(100) if x%5==0 x%2==0]
#[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
[x if x%5==0 and x%2==0 else None for x in range(100)]
#[x if x%5==0 and x%2==0 for x in range(100)]
