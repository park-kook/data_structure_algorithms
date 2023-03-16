'''

a = [abc, a"bc, d;fc]

condition1 if string has " in the one of the strings, then ""
condition2 if string has ; in the one of the strings, then "sting"
condition3 abc; a"bc; d;fc

def 
convert array of strings into one string python

'''

array = ['abc', 'b"cd', 'e;fg']
s='a"bc'

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
