

##########ordered
def ordered_seq_search(arr,ele):
    """
    Sequential search for an Ordered list
    Input array must be ordered!
    """
    # Start at position 0
    pos = 0
    
    # Target becomes true if ele is in the list
    found = False
    
    # Stop marker
    stopped = False
    
    # go until end of list
    while pos < len(arr) and not found and not stopped:
#    while pos < len(arr) and found == False and stopped == False:        
        # If match
        if arr[pos] == ele:
            found = True
            
        else:
            
            # Check if element is greater
            if arr[pos] > ele:
                stopped = True
                
            # Otherwise move on
            else:
                pos  = pos+1
    
    return found

arr = [1,2,3,4,6,9]
sorted_arr = arr.sort() 
