'''
https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/

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


'''
option 2

Time Complexity: O(N^2)
Space Complexity: O(N)
'''
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def isBalanced(rott):
    #base condition
    if root is None:
        return True
    #for left and right subtree height
    lh = height(root.left)
    rh = height(root.right)
    
    # allowed values for (lh - rh) are 1, -1, 0
    if (abs(lh-rh) <=1 ) and isBalanced(root.left) is True and isBalanced(root.right) is True:
        return True
    
    #if we reach here means tree is not
    #height-balanced tree
    return False



'''
option 3


Time Complexity: O(N)
Space Complexity: O(N)
'''
# utility class to pass height object
class Height:
    def __init__(self):
        self.height = 0
 
# function to find height of binary tree
def height(root):
     
    # base condition when binary tree is empty
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1
 
# helper function to check if binary
# tree is height balanced
def isBalanced(root):
    # Base condition when tree is
    # empty return true
    if root is None:
        return True
 
    # lh and rh to store height of
    # left and right subtree
    lh = Height()
    rh = Height()
     
    # Calculating height of left and right tree
    lh.height = height(root.left)
    rh.height = height(root.right)
 
 
    # l and r are used to check if left
    # and right subtree are balanced
    l = isBalanced(root.left)
    r = isBalanced(root.right)
 
    # height of tree is maximum of
    # left subtree height and
    # right subtree height plus 1
 
    if abs(lh.height - rh.height) <= 1:
        return l and r
 
    # if we reach here then the tree
    # is not balanced
    return False
 
# Driver function to test the above function
"""
Constructed binary tree is
            1
        / \
        2     3
    / \ /
    4 5 6 / 7
"""
# to store the height of tree during traversal
 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)
 
if isBalanced(root):
    print('Tree is balanced')
else:
    print('Tree is not balanced')
 
# This code is contributed by Shubhank Gupta
