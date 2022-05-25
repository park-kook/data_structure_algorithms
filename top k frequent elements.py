'''
Top K frequent elements
Given an integer array nums and an integer k, return the k most frequent elements you may return 
the answer in any order. 

Bucket sort
'''
nums = [1,1,1,2,2,3]
k=2
output = [1,2]

def topKFrequent(nums,k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]
    
    for n in nums:
        count[n] = 1+ count.get(n,0) #{1: 3, 2: 2, 3: 1}
    for n,c in count.items():
        freq[c].append(n) #[[], [3], [2], [1], [], [], []] most frequent sotred in index
        
    res = []
    for i in range(len(freq)-1,0,-1): #so inversed order
#        print(i)
        for n in freq[i]:
            res.append(n)
            if len(res) ==k:
#                print(res)
                return res
topKFrequent(nums,k)
