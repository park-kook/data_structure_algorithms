'''
given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. 
input nums1 = [1,3], nums2=[2]
output = 2

nums1 = [1,2], nums2=[3,4]
output = 2.5
(2+3)/2

'''
def findMedianSortedArrays(nums1,nums2):
    A,B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total //2
    if len(B)  < len(A):
         A,B = B,A
    l,r = 0, len(A)-1
    while True: 
        i = (l+r)//2 #A
        j = half - i -2 #B
        
        Aleft = A[i] if i >=0 else float("-infinity")
        Aright = A[i+1] if (i+1)< len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j+1] if  (j+1) < len(B) else float("infinity")
        
        #partition is correct
        if Aleft <=Bright and Bleft <=Aright:
            #odd
            if total %2:
                return min(Aright, Bright)
            
            #even
            return (max(Aleft, Bleft)+ min(Aright, Bright))/2
        elif Aleft>Bright:
            r=i-1
        else:
            l = i+1
            
findMedianSortedArrays(nums1,nums2)            
            
