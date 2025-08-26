'''
head->[16]->[13]->[7] -> None
16->13->1->7Hi
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
      
      '''
      the head of the list is simply a reference to the first node:
      so head is not an "empty node"
      it literally points to the object that contains data=16 and next=node2. 
      '''
