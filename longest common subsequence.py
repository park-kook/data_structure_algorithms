'''
Longest Common Subsequence
Given two strings text 1 and text 2, return the length of their longest common subsequence.

A subsequence of a sting is anew string generated from the original string with some characters 
(can be none)
deleted without changing the relative order of the remaining characters. (eg. "ace" is a subsequence of "
abcde" while "aec" is not). A common subsequenceof two strings is a subsequence that is common to 
both strings. 
'''
text1 = "abcde"
text2 = "ace"
output = 3
1+window.get(s[r],0)


#O(n*m)
def longestCommonSubsequence(text1, text2):
    dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)] #m+1 * n+1 matrix
    
    for i in range(len(text1)-1, -1, -1):
        for j in range(len(text2)-1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1+dp[i+1][j+1] # it matches, goes to the diagonal
            else: 
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])
    return dp[0][0]
longestCommonSubsequence(text1, text2)    



def longestCommonSubsequence(text1, text2):
    dict_1={}
    
    for t in text1:
        if t not in dict_1:
            dict_1[t] = 0
    
    for t2 in text2:
        if t2 in dict_1:
            dict_1[t2] =1+ dict_1.get(t2,0)
    return sum(dict_1.values())
longestCommonSubsequence(text1, text2)
