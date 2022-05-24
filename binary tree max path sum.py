
Binary Tree Maximum Path Sum
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge
connecting them. A node can only appear in the sequence at most once. Note that path does not need to 
pass through the root. The  path sum of a path is the sum of the nodes' values nin the path
Given the root of binary tree, return the maximum path sum of any path
           1
        /    \ 
       2      3
            /   \
            4   5
'''
#root = [1,2,3]
#output = 6
#root = [1,2,3, 4, 5]
#answer = 12

class node:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

def maxPathSum(root):
    res = [root.val] #global variable: why list? we can update it with recursive function
    
    #return max path sum without split
    def dfs(root):
        if not root:
            return 0
        
        leftMax = dfs(root.left)  #recursive function
        rightMax = dfs(root.right)
        leftMax = max(leftMax,0) # if value is negative, equal to zero
        rightMax = max(rightMax, 0) 
        
        #1. compute max path sum with splits
        res[0] = max(res[0], root.val + leftMax + rightMax)
        return root.val + max(leftMax, rightMax) #-> res[0] #2. without split, we cannot choose both. Choose one of them
        
       #between 1 and 2 compete to choose max number for split or without split
   
    dfs(root) # call dfs function with root input to update global variable res above
    return res[0]

root = None
root = node(1)
root.left = node(2)
root.right = node(3)
root.right.left = node(4)
root.right.right = node(5)

maxPathSum(root)  ##12 = = 3+4+5
