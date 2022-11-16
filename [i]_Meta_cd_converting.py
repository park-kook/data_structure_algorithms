'''
cd converting
| cwd      | cd (arg)       | output
| -------- | -------------- | ------
| /        | foo            | /foo
| /baz     | /bar           | /bar
| /foo/bar | ../../../../.. | /
| /x/y     | ../p/../q      | /x/q
| /x/y     | /p/./q         | /p/q

func(cwd, cd) -> new_cwd


cwd="/"
cd="foo"

cwd="/foo/bar"
cd="../../../../.."

cwd="/baz"
cd="/bar"
 
cwd="/x/y"
cd="../p/../q"


cwd="/x/y"
cd="/p/./q"
'''
def fund(cwd,cd):
  cwd_l = cwd.split('/')
  cd_l = cd.split('/')
  res =''
  if cd_l[0]=='': #if cd starts from / then delete all currnet path. 
    cwd_l=[]
  if cwd =='/':
    cwd_l.pop()
    
  for i in range(len(cd_l)):
    if len(cwd_l) >0 and cd_l[i] =='..':
      cwd_l.pop()
      continue #cd_l == '..' remove in the loop      
    elif cd_l[i] =='.':
      continue
    cwd_l.append(cd_l[i])
  res = '/'.join(cwd_l)
  return '/' if len(cwd_l)==0 else res

func(cwd,cd)
    
    
    
    
  
  

