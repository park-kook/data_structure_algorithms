'''
construct binary tree from preorder and inorder traversal
Given preorder and inorder traversal of a tree, construct the binary tree. 
you may assume that dulpicatge do not exist in the tree
preorder = [3,9,20,15,7] - root->left->rigjt
inorder = [9,3,15,20,7] -left->root->right

           3
        /    \ 
       9      20
            /   \
            15   7
output=[3,9,20,null,null,15,7]
'''
from typing import List
class TreeNode: 
    def __init__(self, val=0):
        self.val=val
        self.left=None
        self.right=None

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]        
def buildTree(self,preorder: List[int], inorder:List[int])-> TreeNode:
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
    root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
    return root
  
  
  
buildTree(preorder, inorder)
root = None
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

buildTree([3,9,20,15,7], [9,3,15,20,7])
