
'''
Given a string, write a Python program to find out all possible permutations of a string. 
Let’s discuss a few methods to solve the problem.
'''
ini_str = "abc"
a=list(ini_str)
a
n=len(ini_str)
n
def toString(List):
    return ''.join(List)

toString(a)

def permute(a,l,n):
    if l==n:
        print(toString(a))
    else: 
        for i in range(l,n):
            a[l],a[i] = a[i],a[l]
            permute(a,l+1,n)
            a[l],a[i]=a[i],a[l]
permute(a,0,n)

for i in range(1,3):
    print(i)
