'''
Validate Binary Search Tree
Given the root of binary tree, determine if it is a valid binary search tree
(BST)
A valid BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than 
    the node's key
    The right subtree of a node contains only nodes with keys greater than
    the node's key
    both the left and right subtree must also be binary search trees. 
Time Complexity O(n)
Space complexity O(1)
'''
class node: 
    def __init__(self, val=0):
        self.val=val
        self.left=None
        self.right=None

def isValidBST(root):
    def valid(node,left,right):
        if not node:
            return True
        if not (node.val < right and node.val >left):
            return False
        #node.val is parent node
        return(valid(node.left,left, node.val) and
               valid(node.right,node.val,right))
    return valid(root, float("-inf"), float("inf"))


root = node(2)
root.left = node(1)
root.right = node(3)
isValidBST(root)
