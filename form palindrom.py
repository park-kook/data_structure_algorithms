

'''
can_form_palindrom(param)
param 
param = 'abba' #true
param = 'abc' #false 
param = 'aaaaa' #true 
param = 'aabbb' #true 'abbba'
param = 'a'
param = 'dcbaaabcdd'
'''


def function(param):

    dict={}
    even =0
    odd = 0
    for i in param:
        dict[i] = 1+dict.get(i,0)

    for value in dict.values():

        if value%2 ==1:
            odd+=1

    
    if odd>1:
        return False
    else:
        return True  

function(param)   
