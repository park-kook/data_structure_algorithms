
seq = [[0,0,1,1,0,1]]

def nested_sum(seq):
    stack = []
    stack.append(seq)
    result = 0
    while stack:
        item = stack.pop()
        if isinstance(item, list):


            for e in item:
                stack.append(e)
        else:
            result += item
    return result

nested_sum(seq)
