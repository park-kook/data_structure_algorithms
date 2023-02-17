'''
valid parentheses
Given a string s containing just the characters '(', ')','{','}','[', and ']', determine if the input string is valid
An input string is valid if:
open brackets must be closed in the same type of brackets. 
open brackets must be closed in the correct order. 
every close bracket has a corresponding open bracket of the same type
input: s='()'
output : true
input s='()[]{}"
output: true
input: s='(]'
output: false
Time complexity o(N), space complexity o(N)
'''


def valid(s):
    initvalid=set('([{')
    check=set('()[]{}')
#    match= set([('(',')'),('[',']'),('{','}')])
    result=[]

    
#    if len(s)%2 !=0:
#        return False
    
    for i in s:
#        if i in alp:
        if i not in check:
            continue
            
        if i in initvalid:  #opened bracket and saved it into the result list with the number of opened bracket
            result.append(i)
        else: 
            if len(result)==0: # starting from closed bracket, no matter what it should be False
                return False
           second = result.pop()

           if (second,i) in match:
               continue
           else: 
               return False
        
    return len(result)==0
        
s='(()'    
valid('()')
valid('(())')
valid('((())')
valid('(()))')

a = [x for x in range(10)]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b = {x:None for x in range(10) }
#dictionary is slower than the list and set
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
               continue
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

    
 '''
 Geeksforgeeks version
 '''
 def areBracketsBalanced(expr):
    stack = []
 
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:
 
            # Push the element in the stack
            stack.append(char)
        else:
 
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Check Empty Stack
    if stack:
        return False
    return True
 
