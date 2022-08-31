'''
Longest Palindromic Substring
Given a string s, find the longest palindromic substing in s. you may assume that the 
maximum lenghth of s is 1,000

'''
s = "babad"
output="bab"
s = "cbbd"
output="bb"

def longestPalindrome(s):
    res = ""
    resLen = 0
    for i in range(len(s)):
        #odd length
        l,r = i, i
        while l>=0 and r<len(s) and s[l]==s[r]:
            if (r-l+1) > resLen:
                res = s[l:r+1]
                resLen = len(res)
#                resLen = r-l+1
            l-=1
            r+=1
        #even length
#The edge case (and reason for the seemingly redundant code) is that the above grabs 
#odd length palindromes by starting with 1 index and expanding outwards. 
#You can grab the even case by doing the while loop again, 
#but initializing the pointers to two indices next to each other rather than the same.
        l,r = i, i+1
        while l>=0 and r <len(s) and s[l]==s[r]:
            if (r-l+1)>resLen:
                res = s[l:r+1]
#                resLen = r-1+1
                resLen = len(res)
            l-=1
            r+=1
    return res

longestPalindrome(s)
'''
