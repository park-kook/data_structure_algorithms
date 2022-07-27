'''
K closest Points to Origin
Given an array of points where points[i] = [xi, yi] represents a p o int on the X-Y plane
and an integer k, return the k closest points to the origin (0,0)
'''
import heapq
def kClosest(points,k):
    minHeap=[]
    for x,y in points:
        distance = x**2 + y**2
        minHeap.append([distance,x,y])
    heapq.heapify(minHeap)
    res=[]
    while k>0:
        distance, x, y = heapq.heappop(minHeap)
        res.append([x,y])
        k-=1
    return res


points = [[1,3],[-2,2],[1,1]]
k=2
kClosest(points,k)
output = [[1,1], [-2,2]]


'''
example
li = [5,7,9,1,3]

heapq.heapify(li)
heapq.heappop(li)
output = 1
'''
