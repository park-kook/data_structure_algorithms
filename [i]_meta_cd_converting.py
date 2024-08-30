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

cwd=['','']
'/'.join(cwd)
outcome: '/'
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
    elif cd_l[i] = !='..' and cd_l[i]!='':
      cwd_l.append(cd_l[i])
  res = '/'.join(cwd_l)
  return res if res!='' else '/'

func(cwd,cd)    
    




def cd(cwd, path):
    # If the path is absolute, start from root
    if path.startswith('/'):
        new_path = path
    else:
        # If the path is relative, append it to the current working directory
        new_path = cwd + '/' + path
    
    # Split the path into components
    path_components = new_path.split('/')
    
    # Initialize an empty list to build the normalized path
    normalized_components = []
    
    for component in path_components:
        if component == '' or component == '.':
            # Skip empty components and current directory references
            continue
        elif component == '..':
            if normalized_components:
                # Pop the last component if '..' is encountered and there's a previous component
                normalized_components.pop()
        else:
            # Add the valid directory name to the list
            normalized_components.append(component)
    
    # Join the normalized components into the final path
    normalized_path = '/' + '/'.join(normalized_components)
    
    return normalized_path

# Example usage
examples = [
    ('/', 'foo'), 
    ('/baz', '/bar'), 
    ('/foo/bar', '../../../../..'), 
    ('/x/y', '../p/../q'), 
    ('/x/y', '/p/./q')
]

for cwd, path in examples:
    result = cd(cwd, path)
    print(f'cwd: {cwd}, cd({path}) -> {result}')

'''
Explanation:

	1.	Path Handling:
	•	If the path starts with /, it’s considered an absolute path and cwd is ignored.
	•	If it’s a relative path, it’s concatenated with cwd using a / as the separator.
	2.	Splitting Path Components:
	•	The combined path is split into components based on the / separator.
	3.	Normalization Logic:
	•	The list normalized_components is used to build the final path.
	•	. (current directory) and empty components are skipped.
	•	.. (parent directory) causes the last component in normalized_components to be removed unless it’s empty (i.e., when already at the root).
	•	All other valid components are added to normalized_components.
	4.	Joining Components:
	•	The normalized path components are joined with / to form the final path.

Example Output:

cwd: /, cd(foo) -> /foo
cwd: /baz, cd(/bar) -> /bar
cwd: /foo/bar, cd(../../../../..) -> /
cwd: /x/y, cd(../p/../q) -> /x/q
cwd: /x/y, cd(/p/./q) -> /p/q

This code replicates the expected behavior without relying on the os module, effectively handling both relative and absolute paths by manipulating the path components manually.
'''


