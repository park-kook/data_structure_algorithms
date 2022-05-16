'''
you have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6'
, '7', '8', '9'. The wheels can rotate freely and wrap around: for example wew can turn '9' to '0'
or '0' to be '9'. Each move consists of turning one wheel one slot. 
The lock initially starts at '0000', a string representing the state of the 4 wheels. 
You are given a list of deadend dead ends, meaning if the lock displays any of these codes, the wheels of the lock
will stop turnning and you will be unablt to open it. 

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number 
of turns required to open the lock, or -1 if it is impossible.


'''

from collections import deque

deadends = ['0201','0101','0102', '1212', '2002']
target = "0202"
output  = 6
#0000->1000->1100->1200->1201->1202->0202
lock = '0000'
turns = 0
def openLock(deadends, target):
    if '0000' in deadends:
        return -1
    
    def children(lock):
        res = []
        for i in range(4):
            digit = str((int(lock[i])+1)%10)
            res.append(lock[:i]+digit+lock[i+1:])
            digit = str((int(lock[i])-1+10)%10)
            res.append(lock[:i]+digit+lock[i+1:])
        return res
    
    q=deque()
    q.append(["0000",0])
    visit = set(deadends)
    while q: 
        lock, turns = q.popleft()
        if lock == target:
            return turns
        for child in children(lock):
            if child not in visit:
                visit.add(child)
                q.append([child, turns +1])
    return -1
            
openLock(deadends, target)
children('0000')
lock='9000'
children('9000')
