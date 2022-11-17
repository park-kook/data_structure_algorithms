'''
valid parentheses
'''


def valid(s):
    initvalid=set('([{')
    check=set('()[]{}')
#    match= set([('(',')'),('[',']'),('{','}')])
    result=[]
    alp = set('abc')
    
#    if len(s)%2 !=0:
#        return False
    
    for i in s:
#        if i in alp:
        if i not in check:
            continue
            
        if i in initvalid:
            result.append(i)
        else: 
            if len(result)==0:
                return False
#            second = result.pop()
            result.pop()
#            if (second,i) in match:
#                return True
#            else: 
#                return False
        
    return len(result)==0
        
s='(()'    
valid('()')
valid('(())')
valid('((())')
valid('(()))')

'''
JPMC interview
'''
# Question: Given a string s containing just the characters "(", ")", "{", "}", "[" and "]", 
# determine if the input string is valid. An input string is valid IF:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Examples:
# Input: s = "()", Output: true
# Input: s = "(]", Output: false 
# Input: s = "{[]}", Output: true

def valid_p(s):
    init_valid = set('([{')
    #check_set = set('(){}[]')
    match = set([('(',')'),('[',']'),('{','}')])
    result = []
    for i in s:
    #    if i not in check_set:
    #        continue
        if i in init_valid:
            result.append(i)
        else:
            if len(result) == 0:
                return False

            second = result.pop()
            if (second,i) in match: 
                return True
            else: 
                return False

    return len(result) ==0

a ={1,2,3,4,5,6....... n}
b = [1,2,3,4,5,6]
0, 1,,,,, , n-1
for n in range(len(a)):
    print(a[n]) 

    [x for in range(10)]
    {x:None for in range(10)}
    
