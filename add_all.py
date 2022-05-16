
def add_all(R,C, t):
    total = 0

    num = R*C
    for i in t:
        if type(i) == list: # check whether i is list or not
            total = total + sum(i)
            
        if type(i) == int:
            total += i
    
    return total/num

add_all(2,3,[[0,0,1,1,0,1]])
