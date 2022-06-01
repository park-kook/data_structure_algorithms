
'''
reverse string
Wirte a function that receives a string. The i nput string is given as an array of characters s.
you must do this by modifying the input array in-place with o(1) extra memory

'''

s = ["h","e","l","l","o"]
output = ["o","l","l","e","h"]

'''
version 1: time :o(n), sapce:o(1) - left and right pointers

'''

def reverseString(s):
    res= []
    l,r = 0, len(s)-1
    while l<r:
        s[l],s[r] = s[r],s[l]
        l,r = l+1, r-1
    return s

reverseString(s)
#output = ["h","e","l","l","o"]    
        
'''
version 2: Time: o(n), space o(n) - stack version

'''        
def reverseString(s):
    stack=[]
    for c in s:
        stack.append(c)
    i=0
    while stack:
        s[i] = stack.pop()
        i+=1
    return s
        
reverseString(s)  
output = ["o","l","l","e","h"]
'''
version 3: Time: o(n), space o(n) - revursion version

'''  
def reverseString(s):
    def reverse(l,r):
        if l<r:
            s[l],s[r] = s[r],s[l]
            reverse(l+1, r-1)
    reverse(0,len(s)-1)
    
    return s
reverseString(s)
output = ["o","l","l","e","h"]



###################
def rev_word3(s):
    
    words=[]
    length=len(s)
    space=[' ']
    i=0 #it' is going to be use the index tracker becuase we will be using a while loop to solve this
    #string remove space between neighbor strings
    while i < length:
        if s[i] not in ' ':
            word_start = i
            while i < length and s[i] not in space:
                i += 1
            words.append(s[word_start:i])
            
        i +=1   
    #return words
    #return " ".join(reversed(words))

    new_string = []
    index = len(words)

    while index:
        index -= 1                    # index = index - 1
        #new_string += words[index] # new_string = new_string + character
        new_string.append(words[index]) # new_string = new_string + character
   # print(' '.join(str(x) for x in new_string))
    #return print(' '.join(str(x) for x in new_string))
    #return print(' '.join(x for x in new_string))
    return print(' '.join(new_string))
rev_word3('Hi John, are you ready to go?')
