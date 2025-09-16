'''
Given anarray of integers, return up to the k most frequest element, 
in the order of frequency dsescending, array nums = [1,1,1,2,2,3] and k=2, output [1,2] 

Return up to the k most frequent elements from nums, ordered by descending frequency. 
If there are fewer than k unique elements, return all of them. 
'''

def top_k_freq(nums, k):
  if not nums or k <=0:
    return []
freq ={}
# count freq of each number in O(n)
for num in nums:
  freq[num] = 1+freq.get(num, 0)# ->{1:3, 2:2, 3:1}

buckets = [[] for _ in range(len(nums)+1):
#max freq can't exceed len(nums), so we allocate len(nums)+1 buckets

# fill buckets by frequency in O(u), where u = number of unique elements ( u<=n)
for num, f in freq.items():
  buckets[f].append(num)

result = []

for f in range(len(nums), 0, -1):
  if not buckets[f]:
    continue
  for num in buckets[f]:#optional tie-break: 
    #sort(bucket[f]) if you want deterministic order within same frequency
    result.append(num)
    if len(result) == k: # stop as soon as we have k
      return result

return result #if fewer than k unique elements exist, return whatever we collected



'''
alternative one
'''
def top_f_frequent(nums, k):
  '''
  return uip to k most frequent elements in nums, in order of descending freqeuncy.
  worset case scenarios n log n or u log u
  '''
  freq = {} 
  for num in nums:
    freq[num] = 1+freq.get(num, 0)

  items = list(freq.items())#-> [(1,3), (2,2), (3,1)] (number, count) pair to sort
  #convert to list of (num, count): O(u), u = number of unique elements
  
  #using key = (-count, num) avoid doing sort + reverse; still o(u log u)
  items.sort(key=lambda pair: (-pair[1], pair[0]))
  #-pair[1] -> higher counts come first (descnding by frequency)
  #[1,3), (2,2), (3,1)] -> (-3,1), (-2,2), (-1,3)
  #pair[0]-> (optional) consistent tie-break by numeric value ascending. 2comes before 5
  #you could also d0 items.sort(key=lambda p: p[1], reverse = True) then items.reverse()

  return [num for num, _ in items[:k]] 

  






