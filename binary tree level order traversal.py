
import collections
import heapq
from collections import deque
from collections import defaultdict
from collections import deque
'''
Merge k sorted arrays (Different Sized Arrays)
           3
        /    \ 
       9      20
            /   \
            15   7
'''
class Node: 
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        
        
def levelOrder(root):
    res = []
    q = collections.deque()
    q.append(root)
    
    while q:
        qLen = len(q)
        level = []
        for i in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
                
        if level:
            res.append(level)
    return res

root = None
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
levelOrder(root)
