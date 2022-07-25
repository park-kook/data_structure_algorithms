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
        visit[c] = True
        
        for neighbor in adj[c]: #A, B, C
#            print(neighbor) #A->B and C, B->C, C->nothing print
            if dfs(neighbor):
                return True
#A->B
#A->C
#B->C  
#[C]->[C,B]->[C,B,A]
        visit[c] = False #{'A': True, 'B': True, 'C': False,}
        res.append(c)
        
    for c in adj:#A, B, C
#        print(c)
        if dfs(c):
            return ""
    res.reverse()
    return "".join(res)
alienOrder(words)
