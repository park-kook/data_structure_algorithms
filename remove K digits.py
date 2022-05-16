'''
given string num representing a non-negative integer num, and an integer K, return the smallest possible integer
after removing k digits from me.
'''
def removeKdigits(num,k):
    stack=[]
    for n in num:
        while k>0 and stack and stack[-1] > n:
            stack.pop()
            k-=1
        stack.append(n)
        
    stack = stack[:len(stack)-k]
    res = ''.join(stack)
    # this stack is currently list, now need to convert to string
        
  
    return str(int(res)) if res else "0" #if it is leading zero, then we need to delete it u sing str(int())
        # if res is empty string zero. 

num="1432219"
k=3

removeKdigits(num,k)
