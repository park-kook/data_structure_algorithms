'''
Remove all adjacent duplicates in string II
you are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters 
from s and removing them, causing the left and the right side of the deleted substring to concatenate together
we repeatedly make K duplicate removals on until we no longer can
return the final string after all such duplicate removals have been made. It is guranteed that the answer is unique

'''
s = "abcd"
k=2
output= "abcd"

s = "deeedbbcccbdaa"
k=3
output= "aa"

s = "caabbbacc"
k=3
output = ''

def removeDuplicates(s, k):
    stack = [] #[char, count]
    for c in s:
        if stack and stack[-1][0] ==c:
            stack[-1][1] +=1
        else:
            stack.append([c,1])
            
        if stack[-1][1] ==k:
            stack.pop()
    res = ""
    for char, count in stack:
        res+=(char*count)
    return res

removeDuplicates(s, k)
