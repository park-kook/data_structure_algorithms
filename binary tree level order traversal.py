'''
Binary Tree level order traversal
Given the root of a binary tree return the level order traversal of its nodes'values 
(i.e. from left to right level by level)
time comlplexity: o(N)
space complexity: o(N)

'''
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
output = [[3], [9, 20], [15, 7]]
'''
class Node: 
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        
        
def levelOrder(root):
            
    if root is None:
           return result
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



'''
average sum by level order using queue BDF
'''
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
            avg = sum(level)/len(level)
            res.append(avg)
#            res.append(level)
    return res


root = None
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
levelOrder(root)
[3.0, 14.5, 11.0]




'''
Inorder Tree Traversal without Recursion using pop and stack

1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then 
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right 
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
            1
          /   \
        2      3
      /  \
    4     5
Step 1 Creates an empty stack: S = NULL

Step 2 sets current as address of root: current -> 1

Step 3 Pushes the current node and set current = current->left 
       until current is NULL
     current -> 1
     push 1: Stack S -> 1
     current -> 2
     push 2: Stack S -> 1, 2
     current -> 4
     push 4: Stack S -> 1, 2, 4
     current = NULL

Step 4 pops from S
     a) Pop 4: Stack S -> 1, 2
     b) print "4"
     c) current = NULL /*right of 4 */ and go to step 3
Since current is NULL step 3 doesn't do anything. 

Step 4 pops again.
     a) Pop 2: Stack S -> 1
     b) print "2"
     c) current -> 5/*right of 2 */ and go to step 3

Step 3 pushes 5 to stack and makes current NULL
     Stack S -> 1, 5
     current = NULL

Step 4 pops from S
     a) Pop 5: Stack S -> 1
     b) print "5"
     c) current = NULL /*right of 5 */ and go to step 3
Since current is NULL step 3 doesn't do anything

Step 4 pops again.
     a) Pop 1: Stack S -> NULL
     b) print "1"
     c) current -> 3 /*right of 1 */  

Step 3 pushes 3 to stack and makes current NULL
     Stack S -> 3
     current = NULL

Step 4 pops from S
     a) Pop 3: Stack S -> NULL
     b) print "3"
     c) current = NULL /*right of 3 */  

Traversal is done now as stack S is empty and current is NULL.

otuput: 4 2 5 1 3

'''
#wrong version
def dfs_iterative(root):
    stack, res = [],[]
    n=root
    while n or len(stack)>0:
        if n: 
            stack.append(n)
            n=n.left

        n=stack.pop()
        res.append(n.val)

        n=n.right

    return res
dfs_iterative(root)



class Node: 
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
#inorder
def dfs_iterative(root):
    stack, res = [],[]
    n=root
    while n or len(stack)>0:
        if n: 
            stack.append(n)
            n=n.left #root = node(1), root.left = node(2), root.left = node(3), after that left is null
        elif stack:
            n=stack.pop() #first pop 4 and save it to n, and append n.val = 4 in to the res list
            res.append(n.val)

            n=n.right
#        else:
#            break
    return res

dfs_iterative(root)

root = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
levelOrder(root)
dfs_iterative(root)

output = [4 2 5 1 3]
