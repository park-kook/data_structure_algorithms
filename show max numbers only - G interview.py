input = [6,2,9,1,1,9,10]
output = [6, 9, 9, 10]
def max_list(arr):
    if len(arr)==0:
        return 0
    
    init = []
    max_n = 0
    for num in arr:
        max_n = max(max_n,num)
        if max_n > num:
            continue
        init.append(max_n)
#    init.append(max_n)
    return init

max_list(input)
