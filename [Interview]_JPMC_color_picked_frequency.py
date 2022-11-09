a=[('blue',5),('red',4),('yellow',1)]
#9,8,7,6,5, 4,3,2,1, 0
output is the name of thje color picked, the colr is picked based on frequency (second element in tuple)
a[0][1]
import random

random.random()

def pickColor(a):
    res = []
    total = 0
    interval_d=[]
    
    for l in a:
     
        x,y = l
        res.append(y)
    total = sum(res)
    
    
    roll = random.randint(0,total-1)         

    if roll>=res[0] :
        result = 'blue'
    elif roll>=res[2]:
        result = "yellow"
    else:
        result = "red"

    return result
pickColor(a)
