'''
Meta interview screnning test
Given a long string, write a method that returns true if the string is a valid number or false otherwise. 
Only integers and decimals should be considered as valid. In other words, only characters allowed are digits, 
"-" and ".". The string can be very long (think millions of characters) and no built-in function/class 
can handle it without overflowing or losing precision.
'''

def valid(s):

    isdigit = set("0123456789.-")
    dotcount=0
    minuscount=0
    stack=[]

    flagDotorM = False
    if len(s) == 0:
        return False
    for i,cha in enumerate(s):
        if cha not in isdigit:
          return False
        if cha == '-' and i!=0:
          return False
        if cha =='-':
          minuscount +=1
          if minuscount >=2:
            return False
    
        if cha =='.':
          dotcount+=1
          if dotcount >=2:
            return False

        if s[i] =='.' :
            if i+1==len(s):# if .  or - is the last character
                return False
            
#            if  s[i-1] not in onlynum:
#                return False

    return True
