
'''
Merge K sorted Lists

li = [5,7,9,1,3]
heapq.heapify(li)
[1,3,9,7,5]

heapq.heappush(li,4)
[1,3,4,7,5,9]

heapq.heappop(li)
1
'''

import heapq
#A linked List node
class node:
#    def __init__(self, val=0, next= None):
    def __init__(self, val):
        self.val = val
#        self.next = next
        self.next = None 
#override the function to make node class work with min-heap
    def __lt__(self, other):
        return self.val < other.val


#utility funciton to print contents of a linked list        
def printList(node):
    while node: 
        print(node.val , end = ' ')
        node = node.next
        
        
#the main function to merge given k'sorted linke lists
#it takes a list of lists list of size 'k' and generate the sorted output
#lists  =[[2, 3, 5], [1, 4, 8], [6, 7, 9]]
#
#for x in lists:
#    print(x)


def mergeKlists(lists):
    
    #create a min-heap using the first node of each list
    pq = [x for x in lists] #[[2, 3, 5], [1, 4, 8], [6, 7, 9]]
    heapq.heapify(pq)
    
    #take two pointers, head and tail, where the head points to the first node
    #of the output list and tail points to its last node
    head = last = None
    
    #run till min-heap is empty
    while pq: 
        #extract the minimum node from the min-heap
        min = heapq.heappop(pq) #extract [1,4,8]
        
        #add the minimum node to the output list
        if head is None:
            head = min
            last = min
        else:
            last.next = min
            last = min
            
        #take the next node from the "same"list and insert it into the min-heap
        if min.next:
            heapq.heappush(pq, min.next)
            
    #return head node of the merged list
    return head
k = 3
lists = [None]*k
#lists = [None for i in range(k)]  
lists[0] = node(2)
lists[0].next = node(3)
lists[0].next.next = node(5)

lists[1] = node(1)
lists[1].next = node(4)
lists[1].next.next = node(8)

lists[2] = node(6)
lists[2].next = node(7)
lists[2].next.next = node(9)
head = mergeKlists(lists)
printList(head)
