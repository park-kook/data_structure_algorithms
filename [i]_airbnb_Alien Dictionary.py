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



######################################################################################

'''
Alien Dictionary - Hard
There is a new alien language that uses the English alphabe. However, 
the order among the letters is unknown to you. 
You are given a list of strings words from the alien langugage's dictionary, where the strings in words
are sorted lexicographically by the rules of this new language. 

Return a string of the unique letters in the new alien lagngugae sorted in lexicographically
increasing order by the new langugage's rules. If there is no solution, return "". If there are 
multiple solutions, return any of them. 

A string s is smaller than a string t if at the first letter where they differ, the letter in s
comes before the letter in t in the alien language. If the first min(s.length, t.length) letteres are 
the same, then s is smaller if and only if s.length < t.length

words = ["wrt", "wrf", "er", "ett", "rftt"]
output = "wertf"
w->e->r->t->f

t->f
w->e
r->t
e->r

words2=["A", "BA", "BC", "C"]
A->B
A->C
B->C

post order dfs
A->B->C
A->C
not store A because this is postorder, A->C, there is no further children
now store C in the output, then back to A and go to B (this is postorder, we have to go to all decendent
and print), and C has been already processed,it means gone to the outputlist, so B print because there is no
decendent, and then A print
CBA
we need to reverse order. ABC
'''
words=["A", "BA", "BC", "C"]
output = "ABC"
words = ["wrt", "wrf", "er", "ett", "rftt"]

output = "wertf"


def alienOrder(words):
    adj ={c:set() for w in words for c in w}
    
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        minLen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            continue
#            return ""
        for j in range(minLen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j]) #{'w': {'e'}, 'r': {'t'}, 't': {'f'}, 'f': set(), 'e': {'r'}}
                #{'A': {'B', 'C'}, 'B': {'C'}, 'C': set()}
                break
    visit = {} #means has been processed or not
    res = []
    
    def dfs(c):
        if c in visit:
            return visit[c]
        visit[c] = True #Visit = {A:'True', B:'True', C:'Ture}
        
        for neighbor in adj[c]: #A-> neighbor: B, C
#            print(neighbor) #A->B and C, B->C,
            if dfs(neighbor):
                return True
#A->B
#A->C
#B->C  
#[C]->[C,B]->[C,B,A]
        visit[c] = False #{'A': False, 'B': True, 'C': True}
        res.append(c) #res = ['A']
        
    for c in adj:#A, B, C
#        print(c)
        if dfs(c):
            return ""
    res.reverse()
    return "".join(res)
alienOrder(words)


 if adj[c]:
     print(True)
 print(False)
c="A"
