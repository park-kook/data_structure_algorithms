'''
Rotate list
Given the head of a linked list, rotate the list to the right by k place
1->2->3->4->5

output = 4->5->1->2->3->
'''

class ListNode:
#    def __init__(self, val=0, next= None):
    def __init__(self, val):
        self.val = val
#        self.next = next
        self.next = None 
        
        
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    
    if not head:
        return head
    
    #get length
    length, tail = 1, head
    while tail.next:
        tail = tail.next
        length +=1
        
    k = k% length
    if k ==0: 
        return head
    
    #move to the pivot and rotate
    cur = head
    for i in range(length - k-1):
        cur = cur.next
    newHead = cur.next # make a new linlied list head
    cur.next = None
    tail.next = head # this one is already the last node of the liked list above
    return newHead

head = None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
k=2
rotateRight(head, k)
