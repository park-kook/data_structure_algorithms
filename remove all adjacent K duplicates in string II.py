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




'''
Problem
Remove duplicate characters in a given string keeping only the first occurrences. 
For example, if the input is ‘tree traversal’ the output will be ‘tre avsl’.

Requirements
Complete this problem on a text editor that does not have syntax highlighting, 
such as a goolge doc!

Solution
We need a data structure to keep track of the characters we have seen so far, 
which can perform efficient find operation. If the input is guaranteed to be in standard ASCII form, 
we can just create a boolean array of size 128 and perform lookups by accessing the index of 
the character’s ASCII value in constant time. But if the string is Unicode then 
we would need a much larger array of size more than 100K, which will be a waste since most of 
it would generally be unused.

Set data structure perfectly suits our purpose. It stores keys and provides constant time search 
for key existence. So, we’ll loop over the characters of the string, and at each iteration 
we’ll check whether we have seen the current character before by searching the set. 
If it’s in the set then it means we’ve seen it before, so we ignore it. 
Otherwise, we include it in the result and add it to the set to keep track for future reference. 
The code is easier to understand:
    

'''
def removeDuplicates(string): 
    result=[] 
    seen=set() 
    
    for char in string: 
        if char not in seen: 
            seen.add(char) 
            result.append(char)
            
    return ''.join(result) 


removeDuplicates('tree traversal')


