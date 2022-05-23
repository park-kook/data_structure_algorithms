'''
Minimum Window Substring
Given two strings s and t, return the miminum window in s which will contain all the char in t. If there 
is no such windoe in s that covers all characters in t, return the empty string ""
note that is there is such a window, it is guaranteed that 
there will always be only one unique minimum window in s
'''
s = "ADOBECCDEBANC"
t = "ABC"
output = "BANC"
def minWindow(s, t):
    if t =="": 
        return ""
    
    countT, window = {},{} # Need={A:1, B:1, C:1}, Have={A:0, B:0, C:0}
    
    for c in t: #going through t to create countT hash map
        countT[c] = 1 + countT.get(c,0)
        
        
    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    l = 0 #left pointer
    for r in range(len(s)):
#        c = s[r]
        window[s[r]] = 1+window.get(s[r],0)
        
        if s[r] in countT and window[s[r]]==countT[s[r]]:
            have +=1
        
        while have == need:
            #update our result
            if (r-l+1) < resLen: #window length is less than result length
                res = [l,r]
                resLen = (r-l +1)
            #pop from the left of our window
            window[s[l]]-=1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -=1
            l+=1
    l, r = res
    return s[l:r+1] if resLen !=float("infinity") else ""

minWindow(s, t)
