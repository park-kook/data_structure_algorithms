'''
Comparing Strings containing Backspaces (medium)#
Given two strings containing backspaces (identified by the character ‘#’),
 check if the two strings are equal.
'''

str1="xy#z" 
str2="xyz#"
output = False

str1="xp#"
str2="xyz##"
output = True


str1="xywrrmp"
str2="xywrrmu#p"
output = True

str1="xy#z" #3 2 0
str2="xzz#" #1 0 0
output = True

str1="xy#z" #3 0
str2="xyz#" #1 0
output = False

str1="xp#"
str2="xyz##"
output = True
def backspace_compare(str1, str2):
    index1 = len(str1)-1   
    index2 = len(str2)-1

    while index1>=0 or index2>=0:
        backspace_count = 0
        while index1 >=0:
            if str1[index1] =='#':
                backspace_count+=1
            elif backspace_count>0:
                backspace_count -=1
            else: 
                break
            index1-=1
            
        backspace_count = 0        
        while index2 >=0:
            if str2[index2] =='#':
                backspace_count+=1
            elif backspace_count>0:
                backspace_count -=1
            else: 
                break
            index2-=1  
#        if index1 <0 and index2<0:
#            return True
#        if index1<0 or index2<0:
#            return False
        if  str1[index1] != str2[index2]:
            return False
        index1-=1
        index2-=1
    
    return True

backspace_compare(str1, str2)
