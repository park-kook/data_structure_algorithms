'''
#Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. 
For this problem, you can falsely "compress" strings of single or double letters.
For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
'''
s = 'AAAABBBBCCCCCDDEEEE'
r=''
#r=()
    
###1. while version
def compress(s):
    
    r="" # empty string
    l = len(s)
    if l ==0:
        return ""
    if l==1:
        return s+"1"
    
    #last = s[0]
    cnt = 1
    i = 1
    while i < l:
        if s[i]==s[i-1]:
            cnt +=1
        else:
            r = r+s[i-1]+str(cnt)
            cnt =1
        i +=1
    r=r+s[i-1]+str(cnt)
    return r

compress('AAAAABBBBCCCC')
compress('ABBC')
