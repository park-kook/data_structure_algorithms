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
Output: ""

'''


def longestPalindrome(s):
  result = ""
  resultLen = 0
  for i in range(len(s)):
    

      
#output even length palindromes for s = "cabbad" output = "abba"
#that's why l = i, r = i+1 as a strating point, and then expand l-=1 and r+=1
  
    l,r =i,i+1
    while l>=0 and r<len(s) and s[l] ==s[r]:
      if r-l+1 >resultLen:
        result = s[l:r+1]
        resultLen = len(result)
      l-=1
      r+=1


      
      
#for output odd length palindromes, the following script should be additionally added
#s = "cababad"
#Output: "ababa"
#this example do not go through the script for even length palindromes above. Only second script below go through
# for output odd length palindromes . 

#The edge case (and reason for the seemingly redundant code) is that the above grabs 
#odd length palindromes by starting with 1 same index and expanding outwards. 
#You can grab the even case by doing the while loop again, 
#but initializing the pointers to two indices next to each other rather than the same.    
    l,r = i,i
    while l>=0 and r<len(s) and s[l] ==s[r]:
      if r-l+1 > resultLen:
        result = s[l:r+1]
        resultLen = len(result)
      l-=1
      r+=1      
 return result
      
      
      
      
