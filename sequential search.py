###############################################
#sequential search 
#ele = element
#arr = array
#pos = position
#######unordered

#True or not for unoredered
#True or not for unoredered
def seq_search(arr,ele):
    """
    General Sequential Search. Works on Unordered lists.
    """
    
    # Start at position 0
    pos = 0
    # Target becomes true if ele is in the list
    found = False
    
    # go until end of list
#    while pos < len(arr) and found==False:
    while pos < len(arr) and not found:        
        # If match
        if arr[pos] == ele:
            found = True
            
        # Else move one down
        else:
            pos+=1
    
    return found

arr = [1,9,2,8,3,4,7,5,6]
print(seq_search(arr,1))
print(seq_search(arr,10))

###print position, not true or false
def seq_search(array,ele):
    position =0
    found = False
    while position <len(arr) and found == False:
        if arr[position]==ele:
            found = True
        else:
            position +=1
            if found == False and position ==len(array)-1:
                return False
    return found


