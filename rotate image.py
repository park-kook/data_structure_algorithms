'''
rotate image
you are given nxn 2D matrix representing an image, rotate the image by 90 degree (clockwise)
you have to rotate the image in-place, which means you have modify the input 
2D matrix directly Do not allocate another 2D matrix and do the rotation 

123
456
789


741
852
963


'''
matrix = [[1,2,3],[4,5,6],[7,8,9]]
output = [[7,4,1], [8,5,2], [9,6,3]]

def rotate(matrix):
    l, r = 0, len(matrix)-1
    
    while l<r:
        for i in range(r-l): #or l:r
            top, bottom = l,r
            
            #save the topleft
            topLeft = matrix[top][l+i]
            
            #move bottom left into top left
            matrix[top][l+i] = matrix[bottom-i][l]
            
            #move bottom right into bottom left
            matrix[bottom -i][l] = matrix[bottom][r-i]
            
            #move top right into bottom right
            matrix[bottom][r-i] = matrix[top+i][r]
            
            #move top left into top right
            matrix[top+i][r] = topLeft
            
        r-=1
        l+=1
        
        
