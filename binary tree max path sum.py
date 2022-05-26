
'''
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

time complexity O(n), where N is number of nodes, since we visit each node not more than 2times.
space complexity O(n), where H is a tree height, to keep the recursion stack. In the average case of 
balanced tree, the tree height H = Log N, in the worst case of skwed tree H = N

          -10
        /    \ 
       9      20
            /   \
           15   7
-10->9->new path = 9 update max_sum->20->15->new path = 15 update max_sum ->7->new path 7<max_sum
->max_Gain = 20+15 =35 -> new path 42(20+15+7) update max_sum-> max_gain = -10+35 =25->new path =-10+9+35 = 34
'''
#root = [1,2,3]
#output = 6
#root = [1,2,3, 4, 5]
#answer = 12 #3+4+5 is the max

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
        
        leftMax = dfs(root.left)  #recursive function - first going to the child node bottom
        rightMax = dfs(root.right) # recursively for the node children to
                                    #compute max gain from the left and right subtrees
        leftMax = max(leftMax,0) # if value is negative, equal to zero, we don't need to go further
        rightMax = max(rightMax, 0) 
        
        #1. compute max path sum with splits
        res[0] = max(res[0], root.val + leftMax + rightMax)
 #       res[0] = max(res[0], root.val + max(leftMax, rightMax)) # if we do not start from new path node, only need to go through root node
           #below return change to res[0] instead of one line below. 
        return root.val + max(leftMax, rightMax) #-> res[0] = root.val + max(leftMax, rightMax)
                                                     ##2. without split, we cannot choose both. Choose one of them
        # return the max gain if continue the same path
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
