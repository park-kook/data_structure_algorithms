
'''
a = [abc, a"bc, d;fc]

condition1 if string has " in the one of the strings, then ""
condition2 if string has ; in the one of the strings, then "sting"
condition3 abc; a"bc; d;fc

def 
convert array of strings into one string python

Version1
'''
output = 'abc;b""cd;"e;fg"'
array = ['abc', 'b"cd', 'e;fg']

res=[]
res_s=""

def converts(array):
    
    res=[]
    res_s=""
    for s in array: 
        res.append(s.replace('"', '""'))
    
    for i, s1 in enumerate(res):
        for j, s2 in enumerate(s1):
            if s2 ==';':
                s1='"' + str(s1) + '"'
        res_s+= s1 + ";"
    res_s = res_s[:-1]   
        
    return res_s

converts(array)


'''
version2
'''
array = ['abc', 'b"cd', 'e;fg']
def converts(array):
    
    res=[]
    res_s=''
    
    
    for i, s1 in enumerate(array):
        for j, s2 in enumerate(s1):
            if s2 ==';':
                s1='"' + s1 + '"'
            if s2 =='"':
                s1=s1.replace('"','""')

        res_s+= s1 + ";"

    res_s = res_s[:-1]   
        
    return res_s

converts(array)
