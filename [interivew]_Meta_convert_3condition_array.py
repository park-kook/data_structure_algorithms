



def converts(array):
  res=[]
  for i in array:
    for j in i:
      if j==';':
        i='"'+i+'"'
      if j='"':
        i=i.replace('"','""')
    res.append(i)
  return ';'.join(res)
converts(array)                
