'''
Longest Substring Without Repeating characters. 
Given a s tring s, find the length of the longest substing without repeating characters.

'''
def lengthoflogestsub(s):
    seen=''
    ans=0
    for char in s:
        if char not in seen:
            seen+=char
            ans = max(ans,len(seen))
        else:
            cut = seen.index(char)
            seen=seen[cut+1:]+char                        
    return ans

lengthoflogestsub('pwwkew')#ske
lengthoflogestsub('abcdeafbdgcbb')#eafbdgc

s = 'pwwkew'
s='abcdeafbdgcbb'


'''
Longest Substing without repeating characters
Given a string, find the length of the longest substring without repeating characters
time complexity O(N)
space complexity O(1)
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
