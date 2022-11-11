
"""
google interview
-------------------------------------------------------------
|  q  |  w  |  e  |  r  |  t  |  y  |  u  |  i  |  o  |  p  |
|  a  |  s  |  d  |  f  |  g  |  h  |  j  |  k  |  l  |  4  |
|  z  |  x  |  c  |  v  |  b  |  n  |  m  |  1  |  2  |  3  |
-------------------------------------------------------------

Inputs:
1) keyboard (2d-list of characters) -- keyboard[0][0] == 'q', keyboard[0][1] == 'w'
2) word (string) -- 'cat'
3) max_jump (int) -- 5 or higher -> True, 4 or lower -> False
max_jum= 5
keyboard[2][2] -> c
keyboard[1][0] -> a ->3
keyboard[0][4] -> t ->5
[[q,w,e,r,t,], ['a','s',


"""
word = 'cat'
max_jump= 5

keyboard = [['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l','4'],['z','x','c','v','b','n','m','1','2','3']]
def validKeyboard(keyboard, word, max_jump):
  row = len(keyboard)
  column = len(keyboard[0])
  coord = []
  length = 0
  for letter in word:
      for i, l_letter in enumerate(keyboard):
          if letter in l_letter:
              j  = l_letter.index(letter)
              coord.append([i,j]) #->[[2,2],[1,0],[0,4]]   
  Falsed = 0

  for i in range(len(coord)-1):
      length = abs(coord[i][0] - coord[i+1][0]) + abs(coord[i][1] - coord[i+1][1])
      if length > max_jump:
          Falsed = 1

  if Falsed:
     return False
  else:                                                    
     return True                                                 
                                  
validKeyboard(keyboard, word, max_jump)
