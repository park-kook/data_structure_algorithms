'''
Convert Binary Search Tree(BST) to greater Tree
Given the root of a BST, convert it to a greater tree such that every key of the original BST is changed
to th eoriginal key plus the sum of all keys greater than the original key in BST. 

As a reminder, a binary search tree is a ree that statifies these constraints:
    the left subtree of a node contains only nodes with k eys less than the node's key. 
    the right subtree of a node contains only nodes with key's greater than the node's key.
    Both the left and right subtress must also be binary search trees. 
    

           4 (30)
        /        \ 
       1(36)    6 (21)
    /   \        /   \
   0(36) 2(35) 5(26) 7 (15)
         \            \
          3(33)        8

Time o(n)
Space o(n)

'''
class node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        
def convertBST(root):
    curSum = 0
    
    def dfs(node):
        if not node:
            return
        
        nonlocal curSum # this is because there is declar in the dfs. reference cursum in the upper scope
        dfs(node.right) # this is reversed in order traversal - right node left
        tmp  = node.val #original node
        node.val +=curSum
        curSum += tmp #original node
        
        dfs(node.left)
    dfs(root)
    return root
        
root = None
root = node(4)
root.right = node(6)
root.left = node(1)
root.left.left = node(0)
root.left.right= node(2)
root.left.right.right = node(3)
root.right.left = node(5)
root.right.right = node(7)        
root.right.right.right = node(8)

convertBST(root)
