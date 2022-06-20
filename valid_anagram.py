'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''
s = "anagram" 
t = "nagaram"
Output: true



s = "rat"
t = "car"
Output: false

def isAnagram(s,t):
    s_d={}
    t_d={}
    if len(s) != len(t):
        return False
    
    for i in s:
        s_d[i] =1+s_d.get(i,0)
        
    for i in t:
        t_d[i] =1+t_d.get(i,0)
        
        
    for i in s_d:
        if s_d[i] != t_d.get(i,0):
            return False
    return True
isAnagram(s,t)
