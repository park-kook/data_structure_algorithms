
    
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
# A->B
# A->C
# B->C        
        for neighbor in adj[c]: #A-> neighbor: B, C
#            print(neighbor) #A->B and C, B->C,
            if dfs(neighbor):
                return True

#[C]->[C,B]->[C,B,A]
        visit[c] = False #{'C': False, 'A': True, 'B': True}
        res.append(c) #res = ['C']
        
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

'''
Interview AirBnB alien dictionary 
# You have found a list of alien words. 
You know for a fact that words in this list are sorted, but you don’t know what the alphabet is. 
You would like to reconstruct the original alphabet in such a way, 
that the ordering between letters would explain the sorting of the list.

#Input: ['ccda', 'ccbk', 'cd', 'a', 'ab', 'abc']
# #Output: ['c', 'a', 'k', 'd', 'b'], ['c', 'd', 'a', 'b' 'k'], ['c', 'a', 'd', 'k', 'b'], ['k', 'c', 'a', 'd', 'b'] # k can go anywhere
# ccda < ccbk 
# d < b
# d>b, c>d, c>a, nothing > b, nothing>c
# c>d>b


1. Compare 2 words in order 
    - We don't get information when 2 letters are the same
    - When we have a difference, then we know the letter from the first word is higher order in the alphabet
    [d > b, c > d, c > a] --> [c > d > b > a (a anywhere after c)] 
    
2. Check all letters present in words are part of alphabet
d: 0
b: 1
c: 0
d: 1
c: 0
a: 1
d:[0,1], b:1, c: 0, a: 1

a: []
d: [b]
b: []
c: [a, d]
k: []

'''
for key, value in adj_list.items():
    print(key)
    print(value)

from collections import defaultdict, Counter, deque
adj_list = defaultdict(set)
in_degree = Counter({c : 0 for word in Input for c in word})

#in_degree2={}
#for i in Input:
#    for j in i:
#
#        in_degree2[j]=1+in_degree2.get(j,0)
{c:0 for word in Input for c in word}        

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
    return "".join(output)


reconstruct(Input)
output[0][0]

Input= ['ccda', 'ccbk', 'cd', 'a', 'ab', 'abc']        
print(reconstruct(Input))

for i in range(1,len(Input)):
    for letter1, letter2 in zip(Input[i-1],Input[i]):
        print(letter1, letter2)
        
from collections import defaultdict
words= ['ccda', 'ccbk', 'cd', 'a', 'ab', 'abc']   
def alienOrder(words):
#    adj = {c:set() for w in words for c in w} 
    adj = defaultdict(list)
    #{'c': set(), 'd': set(), 'a': set(), 'b': set(), 'k': set()}
    for i in range(1,len(words)):
        w1, w2 = words[i-1], words[i]
        min_len = min(len(w1),len(w2))
#        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
#            return ""
        for j in range(min_len):
            if w1[j]!=w2[j]:
#                adj[w1[j]].add(w2[j])
                adj[w1[j]].append(w2[j])
                break
    visit={}
    res = []
    def dfs(c):
        if c in visit:
            return True
        visit[c] = True
        for n in adj[c]:
            if dfs(n):
                return True
        res.append(c)
        visit[c] = False
        
    
    for c in adj:
        if dfs(c):
            return ""
    return "".join(res[::-1])
alienOrder(words)


for c in adj:
    print(c)
'''
Sorting Dict by value & storing sorted keys in Dict_keys
'''
s='bbbaaccde'
s='bbaaaccde'
sorted(s)
Dict={}

for x in sorted(s):
    Dict[x]=Dict.get(x,0)+1  
Dict_keys=sorted(Dict, key=Dict.get, reverse=True)  
Dict_keys    
for key in Dict_keys[:3]:
    print(key,Dict[key])  

Dict['b'] = 1
#Dict.items()
#Dict.values()
Dict.get('b',0) # give me the value of 'b' in dict, unless 'b' isn't there in which case give me 0

#Sorting Dict by value & storing sorted keys in Dict_keys.
print(*Dict_keys)

s[::-1]

##########

        


