##########
'''
permutation 
Given an array nums of distinct integers, return all the possible permutations,
you can return the answer in any order
#from three, after pop in the num in the first order using pop(0), two. From two, after pop, it is one legnth
''' 
nums=[1,2,3]
output = [[1,2,3], [1,3,2], [2,1,3], [3,1,2], [3,2,1]]
nums=[0,1]
output = [[0,1],[1,0]]
nums = [1]
output=[[1]]
def permute(nums):
    result = []
    
    #base case
    if (len(nums)==1):
#        return [nums.copy()] #any change(append, remove, change of value) in one list is reflected
        #on both. but when we use the list.copy() method, change made to one list 
        #or not reflected on other except for in nested elements
        return [nums.copy()]
#        return [nums[:]]
    
    for i in range(len(nums)):
        n=nums.pop(0) #from three, after pop, two. From two, after pop, it is one legnth
        
        perms = permute(nums) # two value instead of three
#        print(perms)
#        [2,3], [3,2] then added 1 for each
        for perm in perms:
            perm.append(n) #added 1 after two [2,3], [3,2], perms =[[3, 2, 1], [2, 3, 1]]
#        print(perms)
        result.extend(perms)
        print(result)
        #X=[1,2,3], X.append([4,5]) =>[1,2,3,[4,5]]
        #X,extend([4,5]) =>[1,2,3,4,5]
        nums.append(n)
        
    return result
permute(nums) 


# a=[[3,2],[2,3]]
# for b in a:
#     b.append(1)
# a.append([1])
# a = [[3,2,1],[2,3,1]]
  
  
