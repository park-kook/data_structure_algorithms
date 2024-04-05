
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
