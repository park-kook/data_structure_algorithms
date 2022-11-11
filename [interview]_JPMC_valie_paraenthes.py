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
