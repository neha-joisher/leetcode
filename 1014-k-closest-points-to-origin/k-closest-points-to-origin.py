class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i in range(len(points)):
            x,y=points[i]
            distance=pow(x, 2) + pow(y, 2) 
            heapq.heappush(heap,(-distance,points[i]))
            if len(heap)>k:
                heapq.heappop(heap)
        heap=[point for distance, point in heap]
        return heap