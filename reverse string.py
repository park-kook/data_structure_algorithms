'''
#This interview question requires you to reverse a string using recursion. 
Make sure to think of the base case here.
'''
def reverse(s):
    #Base Case
    if len(s) <=1:
        return s
    #Recursion
    return reverse(s[1:])+s[0]

def reverse(s):
    output=[]
    index=len(s)
    while index:
        index-=1
        output.append(s[index])
    return ''.join(output)

reverse('hello')
reverse('hello world')
reverse('123456789')
