'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Time Complexity: O(N)
Space Complexity: O(N)
'''
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalancedHelper(root):
    #An empty tree is balanced and has height -1
    if not root:
        return True, -1
    #check subtrees to see if they are balanced. 
    leftIsBalanced, leftHeight = isBalancedHelper(root.left)
    if not leftIsBalanced:
        return False, 0
    rightIsBalanced, rightHeight = isBalancedHelper(root.right)
    if not rightIsBalanced:
        return False, 0
    
    #if the subtrees are balanced, check if the current tree is balanced
    #using their height
    
    return (abs(leftHeight - rightHeight)<2), 1+max(leftHeight, rightHeight)

def isBalanced(root):
    return isBalancedHelper(root)[0]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)
isBalanced(root)
