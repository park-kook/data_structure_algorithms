'''
# Amazon - Given a rectangular matrix, we can move from the current cell in 4 directions with
# equal probability.  Calculate the probability that after N moves from a given position (x0, y0) 
# in the matrix (x0,y0 both integers)
# we will not cross boundaries of the matrix at any point, where the x-limits are [0, n - 1]
# and the y limits are given by [0, m - 1]
# matrix size (m,n)
# coordinate of starting point (x,y)
'''

def isSafe(x, y, m, n):
    return (x >= 0 and x < m and
            y >= 0 and y < n)

def prob_matrix(x,y,m,n,N):
    if not (x>=0 and x<m and y>=0 and y<n):
        return 0
    if N==0:
        return 1
    prob=0
    
    prob+=prob_matrix(x,y+1,m,n,N-1)*0.25
    prob+=prob_matrix(x,y-1,m,n,N-1)*0.25
    prob+=prob_matrix(x+1,y,m,n,N-1)*0.25
    prob+=prob_matrix(x-1,y,m,n,N-1)*0.25
    
    return prob
m=5
n=5
x=-1
y=1
N=2
prob_matrix(1,1,5,5,2) #0.875
prob_matrix(0,0,5,5,2) #0.375
isSafe(-11,1,5,5)

prob_matrix(1,1,3,3,2) #0.75
0.625, 0.125, 0.625
0.125, 0.0  , 0.125
0.0625,0.125, 0.0625

prob_matrix(1,0,3,3,1) for first move
0.0625 for x+1
0.0625 (0.25*0.25) for x-1
0 for y-1
0.25 for y+1 (prob_matrix(1,1,3,3,0) for second move)


