

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
        self.key, self.val = key, val
        self.prev = self.next = None
        
class LRUCache:
    def __init__(self, capacity:int):
#    def __init__(self, capacity):
        self.cap = capacity
        self.cache ={} #map key to node
        
        #left = LRU, right = most recent
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left #swap when touch the most recent
        
        #remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        #prev, nxt are pointers
        #remove the middle of them
        
        #insert node at right
    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node #node will be inserted in the middle of them
        node.next, node.prev = nxt, prev
        
        
    def get(self,key:int)->int:
#    def get(self,key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1
    
    def put(self, key:int, value: int)->None:   
#    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache) >self.cap:
            #remove from the linked list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

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
