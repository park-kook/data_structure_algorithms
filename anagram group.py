'''
Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''
#pip install collections-extended
from collections import defaultdict
import collections

    def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
    
groupAnagrams(["eat","tea","tan","ate","nat","bat"])
strs=["eat","tea","tan","ate","nat","bat"]

for s in strs: 
    tuple(sorted(s)))
    
a="eat"
b="tea"    
ans[tuple(sorted(a))].append(a)
ans[tuple(sorted(b))].append(b)
print(ans.keys())
print(ans.values())
