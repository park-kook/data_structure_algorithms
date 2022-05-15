
'''
You're playing Battleship on a grid of cells with 

R rows and C columns. There are 0 or more battleships on the grid, each occupying a single distinct cell. 
The cell in the ith row from the top and jth column from the left either contains a battleship (
Gi,j=1

Gi,j=1) or doesn't (Gi,j=0).
You're going to fire a single shot at a random cell in the grid. You'll choose this cell uniformly at random 
from the R∗C
 possible cells. You're interested in the probability that the cell hit by your shot contains a battleship.
Your task is to implement the function getHitProbability(R, C, G) which returns this probability.

'''
############

from typing import List

# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  numerator = 0
  denominator = R*C
  for i in G:


    if type(i) == list:
      numerator += sum(i)

  
  return format(numerator/denominator,'.8f')

R = 2
C = 3
G = [[0, 0, 1], [0, 0, 1]] #expected value
getHitProbability(R,C,G)
