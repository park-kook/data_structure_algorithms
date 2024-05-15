
'''
Graph Valid Tree
Given n ndoes labeled from 0 to n01 and a list of undirected edges (each h edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree. 
1) There is no cycle. 
2) The graph is connected.
0 1, 1 2, 2 3, 0 2 
true 

0 1, 1 2, 2 3 
false
'''
n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]

output = True

def validTree(n, edges):
    if not n: 
        return True
    adj = {i:[] for i in range(n)}
    for n1, n2 in edges:
        print([n1,n2])
        adj[n1].append(n2)
        adj[n2].append(n1)
#{0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0], 4: [1]}        
    visit = set()
    def dfs(i, prev):
        if i in visit:
            return False
        
        visit.add(i)
        for j in adj[i]:
            if j == prev:
                continue
            if not dfs(j,i):
                return False
        return True
    return dfs(0,-1) and n == len(visit)
validTree( n, edges)

