'''
can_form_palindrom(param)
param 
param = 'abba' #true
param = 'abc' #false 
param = 'aaaaa' #true 
param = 'aabbb' #true 'abbba'
param = 'a' #true 
param = 'dcbaaabcdd' #false
'''

def function(param):
  dict = {}

  odd = 0
  
  for i in param:
    dict[i] = 1+dict.get(i,0)
    
  for key,value in dict.items():
    if value%2 == 1:
      odd+=1
      
  if odd>1:
    return False
  return True

function(param)
