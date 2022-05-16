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
