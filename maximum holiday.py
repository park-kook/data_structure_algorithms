  
'''
Meta
maximum holiday
'''

l_list=['W','W','H','H','W','W','H']
pto=1
count['H']
count['H']
count.get('H',0)
count.values()

def findh(l_list,pto):
    count={}
    res=0
    l=0
    
    for r in range(len(l_list)):
        count[l_list[r]]=1+count.get(l_list[r],0)
        
        while (r-l+1) - count.get('H',0) >pto:
            count[l_list[l]] -=1
            l+=1
            
        res = max(res,r-l+1)
    return res

findh(l_list,pto)
