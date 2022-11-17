'''
#Input: words[] = {“baa”, “abcd”, “abca”, “cab”, “cad”} Output: Order of characters is ‘b’, ‘d’, ‘a’, ‘c’

# You have found a list of alien words. You know for a fact that words in this list are sorted, 
#but you don’t know what the alphabet is. You would like to reconstruct the original alphabet in such a way, 
that the ordering between letters would explain the sorting of the list.
'''
def alienOrder(self, words: List(str))->str:
    adj = {c:set() for w in words for c in w}
    # Build a graph for topological sort
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]
            # Invalid case. w1 should be after w2
            return ""
        for j in range(min_len):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break
    visit = {}
    res = []
    # post-order dfs and check if there is a circle
    def dfs(c):
        if c in visit:
            # there is a circle
            return True
        visit[c] = True
        for n in adj[c]:
            if dfs(n):
                return True
        res.append(c)
        visit[c] = False
    for c in adj:
        if dfs(c):
            # Invalid case
            return ""
    returun "".join(res[::-1])
    
    
    
    
    
    
    
    
    [d > b, c > d, c > a]
Input = ['ccda', 'ccbk', 'cd', 'a', 'ab', 'abc']
def reconstruct(Input):
    in_degree2 = {c:0 for word in Input for c in word} 
    adj_list = defaultdict(list)
    output = []
    for i in range(1,len(Input)):
        for letter1, letter2 in zip(Input[i-1],Input[i]):
            if letter1 != letter2:
#                if letter2 not in adj_list:
                adj_list[letter1].append(letter2)
                in_degree2[letter2]+=1
                
                
#                output.append((letter1,letter2))               
                break
            
    queue = deque([c for c in in_degree2 if in_degree2[c] == 0])
    
    while queue: 
        c = queue.popleft()
        output.append(c)
        
        for d in adj_list[c]:
            in_degree2[d]-=1
            if in_degree2[d]==0:
                queue.append(d)
                
                
    # If not all letters are in output, that means there was a cycle and so
    # no valid ordering. Return "" as per the problem description.
    if len(output) < len(in_degree):
        return ""
    return "".join(output)


reconstruct(Input)
output[0][0]
