'''
Medium encode and deconde
Design an algorithm to encode a list of strings to a string. The encoded string is then sent
over the network and is decoded back to the original list of strings. 

["neet","code"] ->"neet#code"->"neetcode"
"neet", "co#de" -> "neet", "co", "de" this is not what they want
[4,5] store in somewhere
4#neet integet always place in the first after #, read 4 from integer
4#neet5#co#de
'''
#param: strs: a list of strings
#@return: encodes a list of strings to a single string+
strs = ["lint","code","love","you"]
def encode(strs):
    res=""
    for s in strs:
        res +=str(len(s)) + "#" + s
    return res
        
str=encode(strs)     
#@param: str: A string
#@return: decode a single string to a list of strings

def decode(str):
    res,i = [],0
    while i < len(str):
        j=i
        while str[j] !="#":
            j+=1
        length = int(str[i:j])
        res.append(str[j+1: j+1+length])
        i = j+1+length
        
    return res
        
decode(str) 
