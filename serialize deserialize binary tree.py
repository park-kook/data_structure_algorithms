'''
serialize and deserialize binary tree
serialization is the process of converting a data structure or object into a sequence of bits so that
it can be stored in a file or memory buffer, or transmitted across a netowrk connection link to be
reconstructed later in the same or another computer environment

Design an algorithm to serialize and deseiralize a binary tree. There is no restriction on how your serializ
ation / deserialization algorighm should work. You just need to ensure that a binary tree can be serialized
to a string and this string can be deseialized to the original tree structure. 
           1
        /    \ 
       2      3
            /   \
            4   5
'''
root = [1,2,3,null, null, 4,5]
class node:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

class Codec: 
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node: 
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] =="N":
                self.i +=1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i+=1
            node.left = dfs()
            node.right= dfs()
            return node
        return dfs()
'''
