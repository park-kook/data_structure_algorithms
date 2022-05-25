'''
Palindromic Substrings
Given a string s, return the number of palindromic substrings in it. 
A string is a palindrome when it readds the same backwards as forward. 
A substring is a contiguous sequence of characters within the string

'''
s="abc"
output = 3 #"a", "b", "c"
s = "aaa"
output = 6 #"a", "a", "a", "aa", "aa", "aaa"

def countSubstrings(s):
    res = 0 
    for i in range(len(s)):
        #odd
        l = r = i
        while l>=0 and r<len(s) and s[l]==s[r]:
            
            
            res +=1
            l-=1
            r+=1
         #even
        l = i
        r = i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            
            
            res +=1
            l-=1
            r+=1 
    return res

countSubstrings(s)


###ver2
def countSubstrings(s):
    res = 0
    for i in range(len(s)):
        res += countPali(s,i,i)
        res+= countPali(s,i,i+1)
    return res

def countPali(s,l,r):
    res = 0
    while l>=0 and r<len(s) and s[l] ==s[r]:
        res+=1
        l-=1
        r+=1
    return res
countSubstrings(s)
