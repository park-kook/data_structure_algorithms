

###################binary s earch
def binary_search(arr,ele):
    
    # First and last index values
    first = 0
    last = len(arr) - 1
    
    found = False
    
    
    while first <= last and found == False: 
   # while first <= last and not found:         
        mid = round((first+last)/2) # or // for Python 3
        
        # Match found
        if arr[mid] == ele:
            found = True
        
        # Set new midpoints up or down depending on comparison
        else:
            # Set down
            if ele < arr[mid]:
                last = mid -1
            # Set up 
            else:
                first = mid + 1
                
    return found
# list must already be sorted!

arr = [1,2,3,4,5,6,7,8,9,10]
binary_search(arr,5)
binary_search(arr,2.2)



###################### (recusion binary search)
def rec_bin_search(arr,ele):
    
    # Base Case!
    if len(arr) == 0:
        return False
    
    # Recursive Case
    else:
        
        mid = round(len(arr)/2)
        
        
        # If match found
        if arr[mid]==ele:
            return True
        
        else:
            
            # Call again on second half
            if ele<arr[mid]:
                return rec_bin_search(arr[:mid],ele)
            
            # Or call on first half
            else:
                return rec_bin_search(arr[mid+1:],ele)
arr = [3]            
rec_bin_search(arr,3)
rec_bin_search(arr,15)     
