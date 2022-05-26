###another type
def minRemoveToMakeValid(s):
    index_to_remove = []
    stack=[]
    for index,value in enumerate(s):
        if value not in '()':
            continue
        if value =='(':
            stack.append(index)
        else: 
            if len(stack)==0:
#         elif not stack:
                index_to_remove.append(index) #) first case
#         else: 
            else: #stack is not empty, there is something there 
                stack.pop()
    index_to_remove +=stack
    string_builder=[]
    
    
    for index,value in enumerate(s):
        if index not in index_to_remove:
            string_builder.append(value)
    return "".join(string_builder)

###

minRemoveToMakeValid('()())()')

output ='()()()'
