def sort2(x):
    ordered=[]
    i=0
    lowest=x[0]
    while len(x)>0:
        for i in range(len(x)):
            if x[i]<=lowest:
                lowest=x[i]#go through all list of x
        ordered.append(lowest)
        x.remove(lowest)
        if len(x)>1:
            lowest=x[0]
    print(ordered)
    
b=[100,3,4,100,34,45]
b=[1,3,4,5,34,45]
sort2(b)
