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
Time Complexity : O(n)
Space complexity : O(N)

'''
from typing import List
class node: 
    def __init__(self, val=0):
        self.val=val
        self.left=None
        self.right=None

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]   
#def buildTree(self,preorder: List[int], inorder:List[int])-> node:
def buildTree(preorder, inorder)-> node:
    if not preorder or not inorder:
        return None
    
    root = node(preorder[0])
    mid = inorder.index(preorder[0])
#    root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
#    root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
    root.left = buildTree(preorder[1:mid+1],inorder[:mid])
    root.right = buildTree(preorder[mid+1:],inorder[mid+1:])
    return root



def printInorder(node):
    if node is None:
        return
 
    
    #first recur on left child
    printInorder(node.left)
    #then print the data of node
    print(node.val,end=' ')
    # now recur on right child
    printInorder(node.right)

def printPreorder(node):
    if node is None:
        return
    #first print the data of node 
    print(node.val,end=' ')    
    #then recur on left child
    printPreorder(node.left)
    # now recur on right child
    printPreorder(node.right)

preOrder = [3,9,20,15,7]
inOrder = [9,3,15,20,7] 

root = buildTree(inOrder, preOrder)    
print("Inorder traversal of the constructed tree is")
printInorder(root)
printPreorder(root)





"""Recursive function to construct binary of size len from
   Inorder traversal in[] and Preorder traversal pre[].  Initial values
   of inStrt and inEnd should be 0 and len -1.  The function doesn't
   do any error checking for cases where inorder and preorder
   do not form a tree """

def buildTree(inOrder, preOrder, inStart, inEnd):
    if inStart > inEnd:
        return None
    # Pick current node from Preorder traversal using
    # preIndex and increment preIndex
    tNode = node(preOrder[buildTree.preIndex])
    buildTree.preIndex +=1
    
    # if this node has no children then return
    if inStart == inEnd:
        return tNode
    
    # Else find the index of this node in Inorder traversal
    inIndex = search(inOrder, inStart, inEnd, tNode.val)
    
    # Using index in Inorder Traversal, construct left
    # and right subtrees
    tNode.left =  buildTree(inOrder, preOrder, inStart, inIndex-1)
    tNode.right = buildTree(inOrder, preOrder, inIndex+1, inEnd)

    return tNode  

def search(arr,start, end, value):
    for i in range(start, end+1):
        if arr[i]==value:
            return i
           
           
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder)-1)    
print("Inorder traversal of the constructed tree is")
printInorder(root)
printPreorder(root)





  
