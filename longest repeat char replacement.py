
'''
Longest Repeating character replacement
You are given a sting s and an integer k. you can choose any character of the string and 
change it to any other uppercase English character. You can perform this operation at most k times
Return the length of the longest substring containing the same letter 
you can get after replacing
'''

s = "AABABBA"
k=1

output = 4

def characterreplacement(s,k):
    count = {}
    res = 0
    l=0
    
    for r in range(len(s)):
        count[s[r]] = 1+count.get(s[r],0)
        
        while (r-l+1) - max(count.values()) >k:
            count[s[l]]-=1
            l+=1
            
        res = max(res, r-1+1)
    return res

s = "ABABBA"
k=2
characterreplacement(s,k)
