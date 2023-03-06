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


cwd="/" #['',''] after split '/'
cd="foo" #['foo']

cwd="/foo/bar" #['','foo','bar']
cd="../../../../.." #['..','..','..','..','..']

cwd="/baz" #['','baz']
cd="/bar" #['','bar']
 
cwd="/x/y" #['','x','y']
cd="../p/../q" #['..','p','..','q']


cwd="/x/y" #['','x','y']
cd="/p/./q" #['','p','.','q']
'''
def fund(cwd,cd):
  cwd_l = cwd.split('/')
  cd_l = cd.split('/')
  res =''
  if cd_l[0]=='': #if cd starts from / then delete all currnet path. 
    cwd_l=[]
  if cwd =='/': #cwd_l = ["",""] then second missing needs to be removed. 
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
    
    
def fund(cwd,cd):
  cwd_l = cwd.split('/')
  cd_l = cd.split('/')
  res =''
  if cd_l[0]=='': #if cd starts from / then delete all currnet path. 
    cwd_l=['']
  if cwd =='/': #cwd_l = ["",""] then second missing needs to be removed. 
    cwd_l.pop()
    
  for i in range(len(cd_l)):
    if len(cwd_l) >1 and cd_l[i] =='..':
      cwd_l.pop()
      #continue #cd_l == '..' remove in the loop      
    if cd_l[i] =='.':
      continue
    elif cd_l[i] = !='..' and cd_l[!='':
      cwd_l.append(cd_l[i])
  res = '/'.join(cwd_l)
  return res if res!='' else '/'

func(cwd,cd)    
    
  
  

