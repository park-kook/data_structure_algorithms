
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

    

#######String permutation######################
#Given a string, write a function that uses recursion to 
#output a list of all the possible permutations of that string.

#For example, given s='abc' the function should return 
#['abc', 'acb', 'bac', 'bca', 'cab', 'cba']


def permute(s):
    out=[]
    if len(s)==1:
#        out=s
        out=s
        
    else:
        for i, let in enumerate(s):
            
            #for every permutation resulting from step 2 and step 3
            for perm in permute(s[:i]+s[i+1:]):
                print('Current letter is: ',let)
                print('perm is', perm)
                #add it to the output
                out+=[let+perm]
                print('current out is:',out)
    return out
        #for every letter in string


