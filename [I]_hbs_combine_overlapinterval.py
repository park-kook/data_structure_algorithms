intervals = [(7, 10), (1, 3), (12, 15), (2, 6)]

# intervals = [(1, 3)(2, 6)(7, 10), (12, 15)]
result = [(1, 10), (12, 15)]

sorted_intervals = sorted(intervals, key=lambda x:x[0])

result = []
for i in sorted_intervals:
    if not result or result[-1][1]+1 < i[0]:
        result.append(i)
   
    else:
        
        result[-1] = (result[-1][0], max(result[-1][1], i[1]))

    
print(result)
