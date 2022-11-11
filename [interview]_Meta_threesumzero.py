'''
#meta mock interview
'''

def threesumzero(arr):
    arr.sort()
    if len(arr)<3:
        return print("None")

    for i in range(len(arr)-2):
        left = i+1
        right = len(arr)-1
        while left<right:
            if arr[i]+arr[left]+arr[right] ==0:
                print(arr[i],arr[left],arr[right])
                left+=1
                return 
            elif arr[i]+arr[left]+arr[right] <0:
                left+=1
            else:
                right-=1
    return print('Null')
                
threesumzero(arr)                
