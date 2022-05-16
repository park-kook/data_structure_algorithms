
'''
Amazon onsite 3
#Given two rectangles, determine if they overlap. The rectangles are defined as a Dictionary, for example:
'''
r1 = {# x and y coordinates of the bottom-left corner of the rectangle
         'x': 2 , 'y': 5,
         
         # Width and Height of rectangle
         'w':4,'h':12}
def calc_overlap(coor1,dim1,coor2,dim2):
    """
    Takes in 2 coordinates and their length in that dimension * this is one dimension.
    """
    
    # Find greater of the two coordinates
    # (this is either the point to the most right
    #  or the higher point, depending on the dimension)
    
    # The greater point would be the start of the overlap
    greater = max(coor1,coor2)
    
    # The lower point is the end of the overlap
    lower = min(coor1+dim1,coor2+dim2)
    
    # Return a tuple of Nones if there is no overlap
    
    if greater >= lower:
        return (None,None)
    
    # Otherwise, get the overlap length
    overlap = lower-greater
    
    return (greater,overlap)


calc_overlap(2,4,5,12)
