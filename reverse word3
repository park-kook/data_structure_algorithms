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
