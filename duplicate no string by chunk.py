s = 'AAABCADDE'
k = 3
chunks = int(len(s)/k)

for index in range(chunks):
    merge = ""
    T = s[index*k : (index+1)*k]
    for ch in T:
        if ch not in merge:
            merge += ch
    print(merge)

