
"""
Merge Two Sorted linked Lists
Merge two sorted linked lists and return it as a new sorted list. The new
list should be made by splicing together the nodes of the first two lists. 

Method 1 (Using Dummy Nodes) 
The strategy here uses a temporary dummy node as the start of the result list. 
The pointer Tail always points to the last node in the result list, 
so appending new nodes is easy. 

The dummy node gives the tail something to point to initially 
when the result list is empty. This dummy node is efficient, 
since it is only temporary, and it is allocated in the stack. 
The loop proceeds, removing one node from either ‘a’ or ‘b’, 
and adding it to the tail. When 

We are done, the result is in dummy.next. 
There are many cases to deal with: either ‘a’ or ‘b’ may be empty, 
during processing either ‘a’ or ‘b’ may run out first, and finally, 
there’s the problem of starting the result list empty, and 
building it up while going through ‘a’ and ‘b’.
"""
#Linked list node
class Node:
#    def __init__(self, val=0, next= None):
    def __init__(self, val=0):
        self.val = val
#        self.next = next
        self.next = None    
        
# creaete & handle list operation       
class LinkedList:
    def __init__(self):
        self.head = None
    
    #method to display the list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.val, end = ' ')
            temp = temp.next
            
    #method to add element to list
    def addToList(self, newVal):
        newNode = Node(newVal)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
        
        
def mergeLists(l1,l2):
    #a dummy node to store the result
    dummy = Node(0)
    
    #tail stores the last node
    tail = dummy
    

    while l1 and l2:
     
        #compare the data of the lists and whichever is smaller is
        #appended to the last of the merged list and the head is changed
        if l1.val < l2.val:
            tail.next = l1 #lower value will be saved in the tail of the list output
            l1 = l1.next #move lefter pointer to the right
        else: 
            tail.next = l2
            l2 = l2.next
            
            #advance the tail
        tail = tail.next
        #if l1 is already exausted or not if not then replace it
        # if any of the list gets completely empty
    #directly join all the elements of the other list    
    if l1: 
        tail.next= l1
    if l2:
        tail.next = l2
        #returns the head of the merged list
    return dummy.next

listA = LinkedList()
listB = LinkedList() 
listA.addToList(5)
listA.addToList(10)
listA.addToList(15)
listB.addToList(2)
listB.addToList(3)
listB.addToList(20)

listA.head = mergeLists(listA.head, listB.head)
print("Merged Linked List is:")
listA.printList()
