
'''
depth - first tree problem
Given a binary tree, get the average value at each level of the trees. 
Input: 
    4
7     9

10 2        6
      6
   2
   
output: [4,8,6,6,2]
'''
#input can be none empty node or always tree input?
#it looks like all interget, can I assume all integer?
#vefore you begin coding, explain out loud how you would like to solve the problem and get feedback from your interviwer
#Depth First Serach using stack - LastIn First Out
# vs 
    #what if we go to breadth first search, then we can go level by level, once we calculate average
#we can go next level and reset the average, then recalculate avg on the second level

class node(object):
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None
    #hash table, my key is depth of the tress and then value can be in the all list of the associated key value
    #can I start the coding?
    #instead of creating dic, I want recurtion, everytime I call
def _collect(node, dict_data,depth = 0):
    if not node: #empty case
        return None
    if depth not in dict_data:
        dict_data[depth] = []
        
    dict_data[depth].append(node.val)
    
    _collect(node.left, dict_data, depth+1)
    _collect(node.right, dict_data, depth+1)
    
def avg_by_depth(node):
    dict_data = {}
    _collect(node, dict_data) #after run left, data = {0:[4],1:[7,9],2:[10,2,6],3:[6],4:[2]}
    
    result = []
    
    i = 0
    while i in dict_data:
        nums = dict_data[i]
        avg = sum(nums) / len(nums)
        result.append(avg)
        i+=1
    
    return result

root = None
root = node(4)
root.left = node(7)
root.right = node(9)
root.left.left = node(10)
root.left.right = node(2)
root.right.right = node(6)
root.left.right.right = node(6)
root.left.right.right.left = node(2)
avg_by_depth(root)

[4,8,6,6,2]
# I wawnt to go through the code by using some example if every case run throgh smoothly         
#data2: {0:(4,1), 1: (16,2)......}
    
class node(object):
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None
        
def _collect(node, dict_data,depth = 0):
    if not node: #empty case
        return None
    if depth not in dict_data:
        dict_data[depth] = (node.val,1)
    else: 
        val, count = dict_data[depth]
        val+=node.val
        count+=1
        dict_data[depth] = (val,count)
        
    
    _collect(node.left, dict_data, depth+1)
    _collect(node.right, dict_data, depth+1)
    
def avg_by_depth(node):
    dict_data = {}
    _collect(node, dict_data) #after run left, data = {0:[4],1:[7,9],2:[10,2,6],3:[6],4:[2]}
    
    result = []
    
    i = 0
    while i in dict_data:
        val,count = dict_data[i]
        avg = val / count
        result.append(avg)
        i+=1
    
    return result
root = None
root = node(4)
root.left = node(7)
root.right = node(9)
root.left.left = node(10)
root.left.right = node(2)
root.right.right = node(6)
root.left.right.right = node(6)
root.left.right.right.left = node(2)
avg_by_depth(root)

dict_data = {0:[4],1:[7,9],2:[10,2,6],3:[6],4:[2]}

node = [[4],[7,9],[10,2,6],[6],[2]]

avg_by_depth(node)
output = [4.0, 8.0, 6.0, 6.0, 2.0]



import collections
import heapq
from collections import deque
from collections import defaultdict
from collections import deque
'''
Merge k sorted arrays (Different Sized Arrays)
           3
        /    \ 
       9      20
            /   \
            15   7
'''
class Node: 
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        
        
def levelOrder(root):
    res = []
    q = collections.deque()
    q.append(root)
    
    while q:
#        qLen = len(q)
        level = [] # each level: top node, first floor, second floor
        for i in range(len(q)):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
                
        if level:
            res.append(level)
    return res

root = None
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
levelOrder(root)
output = [[3], [9, 20], [15, 7]]

'''
average sum by level order using queue BDF
'''
def levelOrder(root):
    res = []
    q = collections.deque()
    q.append(root)
    
    while q:
        qLen = len(q)
        level = []
        for i in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
                
        if level:
            avg = sum(level)/len(level)
            res.append(avg)
#            res.append(level)
    return res


root = None
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
levelOrder(root)
[3.0, 14.5, 11.0]

'''
###breadth First Search - queue FIFO
'''
a = [1,2,3]
a.pop(0)

queue = []
queue.append('a')
queue.append('b')
queue.append('c')
queue.pop(0)


q = Queue()
q.put('a')
q.put('b')
q.put('c')

q.get()
q.queue[1]
    #what if we go to breadth first search, then we can go level by level, once we calculate average
#we can go next level and reset the average, then recalculate avg on the second level
  #     4
    # / \
    # 2 9
    # / \ \
    # 3 5 7
from queue import Queue

class newNode:
    def __init__(self, a):
        self.val = a
        self.left = None
        self.right = None
        
 '''
using dequeu
'''
def averageOfLevels(root):
    q = deque()
    q.append(root)
    while q:
        Sum = 0
        count = 0
        temp = deque()
        while q:
            n = q.popleft()
#            q.get() #fifo return initial value in the queue
            Sum += n.val
            count+=1
            if (n.left !=None):
                temp.append(n.left)
            if (n.right !=None):
                temp.append(n.right)
        q = temp
        print((Sum*1.0 / count), end = " ")


        
        
        
'''
using Queue
'''
def averageOfLevels(root):
    q = Queue()
    q.put(root)
    while (not q.empty()):
        Sum = 0
        count = 0
        temp = Queue()
        while (not q.empty()):
            n = q.queue[0]
            q.get() #fifo return initial value in the queue
            Sum += n.val
            count+=1
            if (n.left !=None):
                temp.put(n.left)
            if (n.right !=None):
                temp.put(n.right)
        q = temp
        print((Sum*1.0 / count), end = " ")

root = None
root = newNode(4)
root.left = newNode(2)
root.right = newNode(9)
root.left.left = newNode(3)
root.left.right = newNode(5)
root.right.right = newNode(7)
averageOfLevels(root)    
output = [4 5.5 5]
