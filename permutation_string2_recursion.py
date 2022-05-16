
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
