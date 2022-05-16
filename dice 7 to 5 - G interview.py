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

  
'''
#Given a dice which roll from 1 t o 5, simulate a uniform 7 sided dice
#because the 5sided dice can not produce 7possible outcomes on a single roll,
we immediately know that we need to
#roll the dice at least twice. If we roll the dice twice we have 25 possible combinations of 
the results of the two 
#rolls. While 25 is not divisible by 7, 21 is. This means we can implment our previous strategy 
of throwing out
#rolls not in our intended range. It's also important to note that we can't expand the solution 
to implment more rolls
#in order to not throw any out, because 5 and 7 are both prime which menas that no exponent of 
5 will be divisible by 7 no matter how high you go
#We will define our range as a section of the 25 possible combinations of rolls. A good way to 
do this is by converting the two rolls into a unique outcome number in the range 1 through 25. 
#we will create this number by taking the rolls, then we take the first roll and 
after subtacting 1 from it we multiply
#it by 5. Now the first roll corresponds with a value of 1-20(0,5,10,15,20). 
Then we take the second roll and add it to the result 
#of the first manipulation. Giving us a range of 1-25. So our final solution is to roll the dice twice.
 Check the 
#manipulated range from 1 to 25, if its greater than 21, do a reroll. Let's see it in actaion. 
'''
from random import randint
def dice5():
    return randint(1,5)

def convert5to7():
    #for constant re-roll purposes.
    while True:
        #roll the dice twice
        roll_1=dice5()
        roll_2=dice5()
        
        #print 'The rolls were {} and {}'.format(roll_1,roll_2)
        
        #convert the combination to the range 1 to 25
        num=((roll_1-1)*5)+(roll_2)
        
        #print 'The converted range number was:",num
#        if num>21:
#            #re-roll if we are out of range
#            continue
#        return num%7+1
    
        if num>21:#why 25 cut? there is no 26, 27, 28 with residuals to be pared with previous paris
            roll_1=dice5()#BK
            roll_2=dice5()#BK
            num=((roll_1-1)*5)+(roll_2)
        else:
            return num%7+1
    
    
    
convert5to7()

ans = [] 
for _ in range(100000): 
    ans.append(convert5to7()) 
sns.distplot(ans,kde=False) 

15%7
15//7
