Longest Substing without repeating characters
Given a string, find the length of the longest substring without repeating characters
'''
s = "abcabcbb"
output=3

def lengthOfLongestSubstring(s):
    charSet= set()
    l = 0
    res = 0
    
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        res = max(res, r-l+1)
    return res

lengthOfLongestSubstring(s)
