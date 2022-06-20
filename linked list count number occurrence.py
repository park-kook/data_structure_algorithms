
'''
Meta Mock Coding Interview


Given the linked list, count number given the occurance. 
1->3->1->2->1->null

can I assume this linked list ending is null, non cycle, this is singlely linked list
'''
class Node:
    #consturcutr to initialize the node object
    def __init__(self, data):
        self.data = data #assign data (any type, integer and string)
        self.next = None #initialize next as null
        
class LinkedList:
    #function to initialize head
    def __init__(self):
        self.head = None
        
    
    #counts the no. of occurence of a node
    #(search_for) in a linked list (head)
    
    def count(self, search_for):
        current = self.head
        count = 0 
#        while(current is not None):
        while(current):

            if current.data == search_for:
                count +=1
            current = current.next
        return count
        
        
        
    # function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data) #allocate the node and put in the data
        new_node.next = self.head #make next of new node as head E (new head)->A (previous head)->B
        self.head = new_node #move the head to point to new node
   
    #utility function to print the linked linkedList
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            

'''
def insertAfter(self,prev_node, new_data):
add a node after a given node
    # 2. Create new node &
    # 3. Put in the data
        new_node = Node(new_data)
 
    # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next A->B(prev_node)->E(new_node)->C->D->Null
 
    # 5. make next of prev_node as new_node
        prev_node.next = new_node        

Add a node at the end
def insertAfter(self, prev_node, new_data):
 
    # 1. check if the given prev_node exists
    if prev_node is None:
        print("The given previous node must inLinkedList.")
        return
 
    # 2. Create new node &
    # 3. Put in the data
    new_node = Node(new_data)
 
    # 4. Make next of new Node as next of prev_node
    new_node.next = prev_node.next A->B->C>D->Null(X)->E->Null
 
    # 5. make next of prev_node as new_node
    prev_node.next = new_node
   
'''
     

llist = None         
llist = LinkedList()
llist.push(1)
llist.push(3)
llist.push(1)
llist.push(2)
llist.push(1)
llist.push(1)
llist.count(1)      
