'''
#simulate a series of coin tosses where 0 is heads and 1 is tails. You could do this:
from random import random
results = []
for x in range(10):
    results.append(int(round(random())))
    
results = [int(round(random())) for x in range(10)]
'''

a=[('blue',5),('red',4),('yellow',1)]

#9,8,7,6,5, 4,3,2,1, 0
output is the name of thje color picked, the colr is picked based on frequency (second element in tuple)
a[0][1]
import random

random.random()

#leetcode #528, random pick with weight
import random
a=[('blue',5),('red',4),('yellow',1)]
def rand_pick(a):

    color_l=[]
    cum_freq=[]
    total=0
    for tup in a: 
        color, freq = tup
        total += freq
        color_l.append(color)
        cum_freq.append(total)



    roll = random.random()*total
    for i, cum_w in enumerate(cum_freq):
        if roll < cum_w:
            return color_l[i]
rand_pick(a)

