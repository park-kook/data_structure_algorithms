
from collections import OrderedDict
'''
LRU (Least Recently Used) Cache discards the least recently used items first. 
This algorithm requires keeping track of what was used when, which is expensive 
if one wants to make sure the algorithm always discards the least recently used item. 
General implementations of this technique require keeping “age bits” for cache-lines and track the “Least Recently Used” cache-line based on age-bits.
Our problem statement is to design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get and put.
* get(key) – Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1. 
And also move the key to the end to show that it was recently used.
* put(key, value) – Set or insert the value if the key is not already present. When the cache reached its capacity, 
it should invalidate the least recently used item before inserting a new item.
first, we add/ update the key by conventional methods. And also move the key to the end to show that it was recently used. 
But here we will also check whether the length of our ordered dictionary has exceeded our capacity, 
If so we remove the first key (least recently used)
The cache is always initialized with positive capacity.



An OrderedDict is a dict that remembers the order in that keys were first inserted. 
If a new entry overwrites an existing entry, the original insertion position is left unchanged. 
Deleting an entry and reinserting it will move it to the end. Ordered dictionary somehow can be used in the 
place where there is a use of hash Map and queue. It has characteristics of both into one. Like queue, 
it remembers the order and it also allows insertion and deletion at both ends. And like a dictionary, 
it also behaves like a hash map. 

popitem():
This method is used to delete a key from the beginning.

popitem(last = True)  
If the last is False then this method would delete a key from the beginning of the dictionary.
This serves as FIFO(First In First Out) in the queue 
otherwise it method would delete the key from the end of the dictionary.

move_to_end(key, last = True)
If the last is True then this method would move an existing key of the dictionary in the end.
Otherwise it would move an existing key of the dictionary in the beginning. 
If the key is moved at the beginning then it serves as FIFO ( First In First Out ) in a queue.
https://www.geeksforgeeks.org/methods-of-ordered-dictionary-in-python/

'''


from collections import OrderedDict
 
class LRUCache:
 
    # initialising capacity
#    def __init__(self, capacity: int):
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    # first, we add / update the key by conventional methods.
    # And also move the key to the end to show that it was recently used.
    # But here we will also check whether the length of our
    # ordered dictionary has exceeded our capacity,
    # If so we remove the first key (least recently used)
#    def put(self, key: int, value: int) -> None:
    def put(self, key, value):
        self.cache[key] = value #added from the end
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False) #delete from the beginning

    # we return the value of the key
    # that is queried in O(1) and return -1 if we
    # don't find the key in out dict / cache.
    # And also move the key to the end
    # to show that it was recently used.
#    def get(self, key: int) -> int:
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key) #And also move the key to the end to show that it was recently used.
            return self.cache[key]
 


cache = None        
cache = LRUCache(2)
cache.put(1, 1) #// it will store a key (1) with value 1 in the cache. 
print(cache.cache) #OrderedDict([(1, 1)])
cache.put(2, 2) #// it will store a key (2) with value 2 in the cache.
print(cache.cache) # OrderedDict([(1, 1), (2, 2)])
cache.get(1) #// returns 1
print(cache.cache) #OrderedDict([(2, 2), (1, 1)])
cache.put(3, 3) #// evicts key 2 and store a key (3) with value 3 in the cache. 
print(cache.cache) #OrderedDict([(1, 1), (3, 3)])
cache.get(2) #// returns -1 (not found) 
print(cache.cache) OrderedDict([(1, 1), (3, 3)])
cache.put(4, 4) #/ evicts key 1 and store a key (4) with value 4 in the cache. 
print(cache.cache) #OrderedDict([(3, 3), (4, 4)])
cache.get(1); #// returns -1 (not found) 
cache.get(3); #// returns 3 
print(cache.cache) #OrderedDict([(3, 3), (4, 4)])
cache.get(4); #// returns 4
print(cache.cache) #OrderedDict([(3, 3), (4, 4)])

cache = LRUCache(2)
cache.put(1, 1)
print(cache.cache)
cache.put(2, 2)
print(cache.cache)
 
# RUNNER
# initializing our cache with the capacity of 2
cache = LRUCache(2)






##################


'''
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache

implment the LRU Cache class:
    
    1)LRUCache (int capacity) initialize the LRU cache with positve size capacity
    2)int get(int key). Return the value of the key if the key exists, otherwise return -1
    3)void put(int key, int value) update the value of the key if the key exists. 
    Otherwise, add the key-value
    4)pair to the cache. if the number of key exceeds the capacity from this operation, 
    evict the least recently used key
    
    O(1) time complexity

'''
input = ['LRUCache', 'put', 'put', 'get', 'put', 'get', 'put', 'get', 'get', 'get']
input =[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
#[2] is capacity, we can add only two value and key
#[1,1] [key, value]- put
#compared to [1,1] (the most recent used value because of [1]), [2,2] is the least recent used value
# this is how tracking the most recent used or the least recent used
#left point will use least recent - head(dummy node)
#right pointer will use the most recent - tail(dummy node)
# so we currently swap [1,1], [2,2] using doubley linked list
#so if we get then [1,1] will be moved to after [2,2] -> [2,2], [1,1]
# get(Return) value using key 1
#by using hashmap and by lookup looking at the key, this is constant. Instead of value init, we can 
#put the pointer to the [1,1] in the value

# in order put [3,3], [2,2] will be deleted, (replaced with the new key 3)
#[1,1], [3,3] with duoble link list
# 

output = [null, null, null, 1, null, -1, null, -1, 3, 4]



class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val #store both key and val
        self.prev = self.next = None #next set to none means the tail of the linked list, and prev set to
        # none then this indicates that the node is the head of the linked list. 

    def __str__(self):
        return '->'.join([str(Node) for Node in self]) 
       
class LRUCache:
    def __init__(self, capacity:int):
#    def __init__(self, capacity):
        self.cap = capacity
        self.cache ={} #map key to node, value is the pointer
        
        #left = LRU, right = most recent
        self.left, self.right = Node(0,0), Node(0,0) #these are dummy nodes for least and most recent nodes
         #if linked list has no right and left then it means
        # it's empty and therefore the node to be added will be both the head and the tail of the LL
        self.left.next, self.right.prev = self.right, self.left #it will be used insert function below
        
        #remove node from list - 1 helper function 
    def remove(self, node):
        prev, nxt = node.prev, node.next #move previous pointer to the middle into the far right
        #the input node in the middle setting up node.prev = prev
        prev.next, nxt.prev = nxt, prev #update: reconnect tail and head by skipping the middle node
        #prev, nxt are nodes
        #prev.next and nxt.prev are pointers
        #remove the middle of them
        
        #insert node at right most position - 2 helper function 
    def insert(self,node):
        prev, nxt = self.right.prev, self.right #starting from far right
        prev.next = nxt.prev = node #node will be inserted in the middle of them
        node.next, node.prev = nxt, prev #reconnect the pointer tothe middle of prev and right
        
        
    def get(self,key:int)->int:
#    def get(self,key):
        if key in self.cache:
            self.remove(self.cache[key]) #update the most update means delete[1,1]
            self.insert(self.cache[key]) #update the most update means insert[1,1] in right position
            return self.cache[key].val
        
        return -1
    
    def put(self, key:int, value: int)->None:   
#    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key]) # if key in the cache, the remove the key first in the cache
        self.cache[key] = Node(key,value) #we put new node in the hashmap pointing to this node
        self.insert(self.cache[key]) #and then this node insert in our list
        
        if len(self.cache) >self.cap:
            #remove from the linked list and delete the LRU from the hashmap
            lru = self.left.next #accoridng to the above
            self.remove(lru) # first, this removes from the linked list
            del self.cache[lru.key] #and also delete this in the hash map

cache = None
cache = LRUCache(2)
cache.put(1,1)
#print(cache.cache)
cache.put(2,2)
#print(cache.cache)
cache.get(1)
#print(cache.cache)
cache.put(3,3)
#print(cache.cache)
cache.get(2)
#print(cache.cache)
cache.put(4,4)
#print(cache.cache)
cache.get(1)
#print(cache.cache)
cache.get(3)
#print(cache.cache)
cache.get(4)
#print(cache.cache)





from collections import OrderedDict
 
class LRUCache:
 
    # initialising capacity
#    def __init__(self, capacity: int):
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
 
    # we return the value of the key
    # that is queried in O(1) and return -1 if we
    # don't find the key in out dict / cache.
    # And also move the key to the end
    # to show that it was recently used.
#    def get(self, key: int) -> int:
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
 
    # first, we add / update the key by conventional methods.
    # And also move the key to the end to show that it was recently used.
    # But here we will also check whether the length of our
    # ordered dictionary has exceeded our capacity,
    # If so we remove the first key (least recently used)
#    def put(self, key: int, value: int) -> None:
    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

cache = LRUCache(2)
cache.put(1, 1)
print(cache.cache)
cache.put(2, 2)
print(cache.cache)
