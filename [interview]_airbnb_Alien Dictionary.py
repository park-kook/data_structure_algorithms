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
