'''
#simulate a series of coin tosses where 0 is heads and 1 is tails. You could do this:
from random import random
results = []
for x in range(10):
    results.append(int(round(random())))
    
results = [int(round(random())) for x in range(10)]
'''

a=[('blue',5),('red',4),('yellow',1)]

#9,8,7,6,5, 4,3,2,1, 0
output is the name of thje color picked, the colr is picked based on frequency (second element in tuple)
a[0][1]
import random

random.random()

#leetcode #528, random pick with weight
import random
a=[('blue',5),('red',4),('yellow',1)]
def rand_pick(a):

    color_l=[]
    cum_freq=[]
    total=0
    for tup in a: 
        color, freq = tup
        total += freq
        color_l.append(color)
        cum_freq.append(total)



#     roll = random.random()*total
    roll = random.randint(1,10)
    for i, cum_w in enumerate(cum_freq):
        if roll < cum_w:
            return color_l[i]
rand_pick(a)







#Approach 1: Prefix Sums with Linear Search
class Solution:

    def __init__(self, w: List[int]):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i
            
import random
#Choose 5 elements from the list with different probability
sampleList = [10, 20, 30, 40]
weight = [10,20,30,40]
x = random.choices(sampleList, weights = weight)
print(x)


#Approach 2: Prefix Sums with Binary Search
class Solution:
    def __init__(self, w: List[int]):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        # run a binary search to find the target zone
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low

