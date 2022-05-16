
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
