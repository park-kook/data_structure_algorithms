'''
Example 1:

s = "cabbad"
Output: "abba"

s = "cabbadd"
Output: "abba"

s = "aacabbade"
Output: "abba"


s = "abcabccbaabc"
Output: "abccba"

s = "cababad"
Output: "ababa"

'''


def longestPalindrome(s):
  result = ""
  resultLen = 0
  for i in range(len(s)):
    
#output even length
    l,r = i,i
    while l>=0 and r<len(s) and s[l] ==s[r]:
      if r-l+1 > resultLen:
        result = s[l:r+1]
        resultLen = len(result)
      l-=1
      r+=1
      
#output odd length
#The edge case (and reason for the seemingly redundant code) is that the above grabs 
#odd length palindromes by starting with 1 index and expanding outwards. 
#You can grab the even case by doing the while loop again, 
#but initializing the pointers to two indices next to each other rather than the same.      
    l,r =i,i+1
    while l>=0 and r<len(s) and s[l] ==s[r]:
      if r-l+1 >resultLen:
        result = s[l:r+1]
        resultLen = len(result)
      l-=1
      r+=1
      
 return result
      
      
      
      
