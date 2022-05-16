
from collections import defaultdict
import collections
'''
Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of continuous 
subarrays whose sum equals to k.

The idea behind this approach is as folows: if the cumulative sum (sum[i] for sum up to ith index) 
up to two indices is the same, 
the sum of the elements lying in between those indices is zero. Extending the same thought further, if the 
cumulative sum up to two indices, say i and j is at a difference of k, i.e. if sum[i] - sum[j] = k 
(=sum[i]-k = sum[j]) 
the sum of elements lying between indices i and j is k. 


'''
 def subarraySum(nums, k):
     
     
     n=len(nums)
     count=0
     #dict_cumsum=defaultdict(int) # hashtable for storing the cumsum we have seen so far
     dict_cumsum={}
     curr_sum = 0 # for cumulative sum at each index
     for i in range(n): # upto the length of the nums array
         curr_sum +=nums[i] # cumulative sum in each index
         if curr_sum == k: #if current cumsum is equal to target 
             count+=1
                         # if curr_sum - k in the dict, then let's say 
            # curr_sum - k = some_val. so, curr_sum = k + some_val, means 
            # if the some_val is already in the dictionary, then there 
            # exists a subarray whose sum is k that has lead us to this
            # curr_sum. How lead us? by some_val + k = curr_sum
            # now if some_val occurs more than 1 time, means you have
            # that number of subarray to consider to the count
            # So you need to add that number of occurence of curr_sum - k
            # to the count
            # think about this with example nums list in the solution 
            # [3,4,7,2,-3,1,4,2] and also with [3,4,7,2,-3,1,4,2, 1]
             
         if curr_sum-k in dict_cumsum:
            count+=dict_cumsum[curr_sum-k]
            
         #dict_cumsum[curr_sum]+=1
         dict_cumsum[curr_sum] = 1
            # add the curr_sum entry to the hashtable
             
        # if curr_sum-k in dict_cumsum:
        #    count+=dict_cumsum[curr_sum-k]
        # else:
        #     dict_cumsum[curr_sum]+=1
     return count
             
nums=[3,4,7,2,-3,1,4,2]
k=7
subarraySum(nums, k)   
subarraySum([1,1,1],2) #2
subarraySum([3,4,7,2,-3,1,4,2],7) #4
subarraySum([1,2,1,2,1],3) #4
subarraySum([1,2,3],3) #2
dict_cumsum={}
dict_cumsum[13]=1
