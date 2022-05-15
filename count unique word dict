v = ['bcdef','abcdefg','bcde','bcdef']
def uniqueWordDict(v):
    num = len(v)
    unique_wordlist=[]
    unique_worddict={}
    
    c=0
    while c<num:
        word = v[c]
        if word not in unique_worddict:
            unique_worddict[word]=0
            unique_wordlist.append(word)
        
        unique_worddict[word]+=1
        c+=1
    
    tempstr=[]
    for word in unique_wordlist:
#        print(unique_worddict[word])
        
    #    print(' '.join(x) for x in str(unique_worddict[word]))
        tempstr.append(unique_worddict[word])
#        tempstr+=str(unique_worddict[word]) + ','
#        tempstr = ','.join(unique_worddict[word])
        
    return tempstr
uniqueWordDict(v)   
