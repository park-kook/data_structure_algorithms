''''
#Google onsite interview
#Given a dice which rolls 1 to 7(with uniform probability), simulate a 5sided dice. Preferly, 
write your solution as a function
# your given a funcion random_7() and you have to take it as an input and create random_5()
# the key to solving this problem is to make sure you focus on the requirement that the final distribution 
of the rolls 
# be uniform, also you were not given any requirements on Time and Space, so the solution is actually 
very simple,
# just keep re-rolling if you get a number greater than 5
'''
from random import randint
import seaborn as sns
def dice7():
    return randint(1,7)

#our solution
def convert7to5():
    
    #starting roll (just need to be larger than 5)

    roll = 7
    while roll >5:
        roll=dice7()
        print('dice7() produced a roll of ',roll)
    print('your final returned roll is below:')
    return roll

convert7to5()

ans = [] 
for i in range(100000): 
#for _ in range(100000): 
    ans.append(convert7to5()) #generate 5 bar
sns.distplot(ans,kde=False) 


################# 6 to 7
import seaborn as sns
from random import randint
def dice36():
    return randint(0,35)

#our solution
def convert6to7():
    
    #starting roll (just need to be larger than 5)

    roll = 35
    while roll >34:
        roll=dice36()
        #print('dice7() produced a roll of ',roll)
    #print('your final returned roll is below:')
    return (roll//5)+1

convert6to7()

ans = [] 
for i in range(100000): 
#for _ in range(100000): 
    ans.append(convert6to7()) #generate 5 bar
sns.distplot(ans,kde=False) 



################# 5 to 7
import seaborn as sns
from random import randint
def dice36():
    return randint(0,24)

#our solution
def convert5to7():
    
    #starting roll (just need to be larger than 5)

    roll = 25
    while roll >20:
        roll=dice36()
        #print('dice7() produced a roll of ',roll)
    #print('your final returned roll is below:')
    return (roll//3)+1

convert5to7()

ans = [] 
for i in range(100000): 
#for _ in range(100000): 
    ans.append(convert5to7()) #generate 5 bar
sns.distplot(ans,kde=False) 


'''
Google onsite interview 2

############################################################################
# Generate a uniform random numbers between 1 and 7 using a six-sided die  
# Idea : roll the die twice and partition the 36 outcomes into sets of 5 each and repeat on 
last pair of outcome  
# __author__ : Vamshi Guduguntla 
 '''
#from scipy.stats import randint  
from random import randint
import seaborn as sns
def die(): 
 #return randint.rvs(low = 1, high = 6+1 ) 
     return randint(1,7)
die()


def get_outcomes(): 
    outcomes = [] 
    for i in range(1,6+1): 
        for j in range(1,6+1): 
            outcomes.append((i,j)) 
    return outcomes 
get_outcomes()


def rand_1_7():
 # Time : O(1)  0
 # Space : O(1) 
 # roll the die twice  
 # Areas for improvement : precompute the get_outcomes() and pass it to the function  
    #res = (die(),die()) 
 # call the outcomes  
    outcomes = get_outcomes() 
    #res = list((die(),die()))
    res = (die(),die())
 # find the index of the die in the outcomes  
 # linear search  
    #idx=0
    for i in range(len(outcomes)): #36: i =  0 ~ 35
        #res = (die(),die()) 
        if res == outcomes[i]: 
            idx = i  
 # condition for re-roll  
    if idx == 35: #36-1=35 due to zero index startm , why 35 cut? there is only one 36 with residual 1
        return rand_1_7() 
    else: 
        #return((idx // 5) + 1) 
        return((idx % 7) + 1) 

rand_1_7()
ans = [] 
for i in range(100000): 
#for _ in range(100000): 
    ans.append(rand_1_7()) 
sns.distplot(ans,kde=False) #generate seven bars




ans[:50]
0%7
len(outcomes)
34//6 #5
0//6 #0
1//6 #0
6//6 #1
35//6#5
rand_1_7() 
    
