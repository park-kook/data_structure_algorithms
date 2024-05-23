'''
Compute the customized sum given a nested list / array. 

Input : [2,[3]]   

1*2 + 2*3  

Output : 8 

  
Input : [2,[[3]]]   

Output : 1*2 + 3*3  = 11 


Input : [2,[3,[4]]]   

1*2 + 2*3 +3*4  

Output : 20
  
'''

nested_list = [1,[2,[3,4],5,[6,7]]]
depth=1
def depth_sum(nested_list, depth=1):
  result = 0
  for i in nested_list:
    if isinstance(i,list):
      result+=depth_sum(i,depth+1)
    else:
      result+=i*depth
return result

depth_sum(nested)list, depth)
