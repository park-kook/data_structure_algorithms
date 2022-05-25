'''
Given a binary tree, print it vertically. The following example illustrates the vertical order traversal.
           1
        /    \ 
       2      3
      / \   /   \
     4   5  6   7
               /  \ 
              8   9 

output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9

'''
    ''' Construct the following tree
            1
          /   \
         /     \
        2       3
              /   \
             /     \
            5       6
          /   \
         /     \
        7       8
              /   \
             /     \
            9      10
    '''
'''

using level order traversal using bfs first in first out

Time Complexity of the above implementation is O(n Log n). of note a Self-Balancing Binary Search Tree where all operations take O(Logn) time. 
hashing based solution can be considered as O(n) 

Auxiliary Space: O(n)
'''
####### Version BFS 1
# Function to perform vertical traversal on a given binary tree
from collections import defaultdict
from collections import deque
def printVertical(root):
    # base case
    if root is None:
        return
    # create a dictionary to store the vertical order of binary tree nodes
#    d={}
    d = defaultdict(list)
    # create an empty queue for level order traversal.
    # `It` stores binary tree nodes and their horizontal distance from the root.

    q=deque()
    
    # enqueue root node with horizontal distance as 0
    q.append((root,0))

    # loop till queue is empty
    while q:
        
        # dequeue front node
        node, dist=q.popleft()
        
        # insert front node value into the dictionary using its horizontal distance
        # as the key
#        if dist not in d:
#            d[dist] = []
        if node is not None:
            d[dist].append(node.key) 

        # enqueue non-empty left and right child of the front node
        # with their corresponding horizontal distance
            q.append((node.left, dist-1))
            q.append((node.right, dist+1))
    
    for key in sorted(d.keys()):
        print(d.get(key))
    

printVertical(root)   



###### Version BFS 2

from collections import defaultdict
def verticalOrder(node):
    columnTable = defaultdict(list)
#    queue = deque([(node,0)])
    queue = deque()
    queue.append((root,0))
    res= []
    while queue: 
        node, column = queue.popleft()
        if node is not None:
            columnTable[column].append(node.key)
            queue.append((node.left, column-1))
            queue.append((node.right, column+1))
#    for x in sorted(columnTable.keys()):
#        res.append(columnTable[x]  )      
    return [columnTable[x] for x in sorted(columnTable.keys())]
#    return res
verticalOrder(root)

root = None
root=node(1)
root.left = node(2)
root.right = node(3)
root.right.left = node(5)
root.right.right = node(6)
root.right.left.left = node(7)
root.right.left.right = node(8)
root.right.left.right.left = node(9)
root.right.left.right.right = node(10)
print("Veticalorder traversal is")
printVerticalOrder(root)

verticalOrder(root)

'''
using preorder traversal
'''
#A binary tree node
# A class to store a binary tree node
class node: 
    # Constructor to create a new node
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        
# Utility function to store vertical order in map 'm'
# 'hd' is horizontal distance of current node from root
# 'hd' is initially passed as 0
def getVerticalOrder(node, horizontalDistance, m):
    #base case
    if not node:
        return None
    
    #store current node in map 'm'
#    try: 
#        m[horizontalDistance].append(root.key)
#    except: 
#        m[horizontalDistance] = [root.key]
    if horizontalDistance not in m:
        m[horizontalDistance] = []
        
    m[horizontalDistance].append(node.key)
#    print(node.key) #preorder       
    #store nodes in left subtree
    getVerticalOrder(node.left, horizontalDistance-1, m)
#    print(node.key) #inorder         
    #store nodes in right subtree
    getVerticalOrder(node.right, horizontalDistance+1, m)
#    print(node.key) #postorder        
def printVerticalOrder(node):
    #create a map and store vertical order in map using function getVerticalORder()
    #function getVerticalORder()
    m = {}
    horizontalDistance = 0
    getVerticalOrder(node, horizontalDistance,m)
    
    #traverse the map and print nodes aat every horizontal distance (hd)
    
    for index, value in enumerate(sorted(m)):
        for i in m[value]:
            print(i, end=" ")
        print()
root = None
root=node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)
root.right.right.left = node(8)
root.right.right.right = node(9)
print("Veticalorder traversal is")
printVerticalOrder(root)


root = None
root=node(1)
root.left = node(2)
root.right = node(3)
root.right.left = node(5)
root.right.right = node(6)
root.right.left.left = node(7)
root.right.left.right = node(8)
root.right.left.right.left = node(9)
root.right.left.right.right = node(10)
print("Veticalorder traversal is")
printVerticalOrder(root)
    ''' Construct the following tree
            1
          /   \
         /     \
        2       3
              /   \
             /     \
            5       6
          /   \
         /     \
        7       8
              /   \
             /     \
            9      10
    '''
    
    
a={2:"c",1:"b",3:"a"}
sorted(a) #[1,2,3]
a.get(2)

