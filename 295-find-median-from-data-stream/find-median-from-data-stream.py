class MedianFinder:

    def __init__(self):
        self.small=[] #Max heap
        self.large=[] #Min heap

    def addNum(self, num: int) -> None:
        
            heapq.heappush(self.small, -1* num)
        
        #1. Every element in Small is <= 
        #   Every element in Large

            if self.large and (-1* self.small[0])>self.large[0]:
                val=heapq.heappop(self.small)
                heapq.heappush(self.large, -val)
            

        #2. Size difference b/w small and large<=1
            if len(self.small)-len(self.large)>=2:
                val=heapq.heappop(self.small)
                heapq.heappush(self.large, -val)

            if len(self.large)-len(self.small)>=2:
                val=heapq.heappop(self.large)
                heapq.heappush(self.small, -val)


    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -self.small[0]
        
        elif len(self.large)>len(self.small):
            return self.large[0]

        return (-self.small[0]+self.large[0])/2
 
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()