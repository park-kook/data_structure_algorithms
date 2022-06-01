'''
check if a string contains all binary codes of size K
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. 
Otherwise, return False

'''
s = "00110110"
k = 2
#"00","01","10","11", They can be all found as substrings at indices 0,1,3, and 2 respectively. 

s="0110"
k=1

def hasAllCodes(s,k):
    codeSet = set()
    
    for i in range(len(s)-k+1):
        codeSet.add(s[i:i+k])
    return len(codeSet) == 2**k

hasAllCodes(s,k)
