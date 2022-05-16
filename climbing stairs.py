'''
climbing stairs - Breadth First Search - bottom up Dynamic programming
you are climbing a staircase it takes n steps to reach the top.
each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

stair [0,1,2,3,4,5]
ways  [8,5,3,2,1,1]
              one,two

8 comes from 5+3 in the previous two
5 comes from 3+2 
this is kind of pibonachi sequence problem. We need to calculate n-1 times
'''
n=2
ouput=2 #1step + 1 step and 2step
n=3 
output=3 #1step + 1 step + 1 step, 2step + 1 step, 1 step + 2steps

def climbStairs(n):
    one, two = 1,1
    for i in range(n-1):
        temp = one #2. before update one, we stor the one in the templary 
        one = one + two #1. one is calcualted by one + two and updated
        two = temp #2. two needs to be shifted
    return one
climbStairs(2)
climbStairs(5)
