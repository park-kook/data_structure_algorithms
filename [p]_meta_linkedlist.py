'''
head->[16]->[13]->[7] -> None
16->13->1->7 insert 1 value between 13 and 7 at 2 index
'''
class SinglyLinkedListNode:
  def __init__(self, data):
    self.data = data
    self.next = None
  def insert(head, data, position):
    new_node = SinglyLinkedListNode(data):
    if position ==0:
      new_node.next = head
      return new_node
    current = head
      
      '''
      the head of the list is simply a reference to the first node:
      so head is not an "empty node"
      it literally points to the object that contains data=16 and next=node2. 
      we are making another reference called current.
      Right now, both head and current pointo the same node object (the one with data=16)
      '''
    for _ in range(position-1):
      current = current.next
      '''
      At first, current points to the node with data = 16.
      THat node's .next points to the node with data = 13.
      So after this line, current now points to the node 13. Suppose slow is poiting at node (10).
      slow.next is node(20)
      by assigning slow = slow.next, we move the reference from node(10) to node(20)
      
      '''
    new_node.next = current.next #1->7
    current.next = new_node #13->1

    return head

node1 = SiglyLinkedListNode(16) #data = 16, next = None
'''
It creates a real object in memory:
data = 16
next = None
When we connect nodes by setting . next, we're wiring those objects together.
'''
node2 = SiglyLinkedListNode(13)  #data = 13, next = None
node3 = SiglyLinkedListNode(7)  #data = 7, next = None
node1.next = node2 #16->13
node2.next = node3 #13->7

'''
head
[16 | next->node2] -> [13|next -> node3] -> [7|next=None]
current
'''

'''
A linked list is said to contain a cycle
if any node is visted more than once while traversing the list. 
Given a pointer to the head of a linked list, determine if it contains a cycle. 
If it does, return. Otherwise, retrurn. 
1->2->3
'''

def has_cycle(head):
  '''
  detects if a linked list has a cycle. 
  Parameters: 
  head (SinglyLinkedListNode): head of the List

  Returns:
  int: 1 if cycle exists, 0 otherwise
  '''
  slow = head
  fast = head
  while fast and fast.next: #while there are nodes ahead
    slow = slow.next #move slow by 1
    fast = fast.next.next #move fast by 2
    if slow == fast: #they meet -> cycle
      return 1
  return 0 #fast reached end -> no cycle

# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2   # 1 -> 2
node2.next = node3   # 2 -> 3
node3.next = None  

node3.next = node2   # instead of None, point back to node2

current = node1
for _ in range(6):  # try moving 6 steps
    print(current.data, end=" -> ")
    current = current.next
# output 1 -> 2 -> 3 -> 2 -> 3 -> 2 ->
'''
why not 2->1?
because singly linked lists only store forward pointers.
even though the list was originally "1->2->3", once we made 3.next = 2,
there is no link that points basck to 1 any more. 
so after entering the cycle, traversal can only bounce between 2 and 3:
from 2->3
from 3->2
Node 1 is "behind" with no arrows pointing back to it, so you can't reachj it again. 
'''

def has_cycle(head):
  '''
  Detects if a linke list has a cycle using a visited set.
  Parameters:
  head(SinglyLInkedisNode): head of the list
  Returns:
  int: 1 if cycle exists, 0 otherwise
  '''
  visited = set()
  current = head
  while current:
    if current in visited: #we've seen this node before -> cycle
      return 1
    cisited.add(current) #mark this node as visited
    current = current.next #move forward
  return 0 #reached end -< no cycle

