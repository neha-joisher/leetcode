class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_Heap=[-i for i in stones]
        heapq.heapify(max_Heap)
        while len(max_Heap)>1:
            x=heapq.heappop(max_Heap)
            y=heapq.heappop(max_Heap)
            print(x,y)
            if x==y:
                continue
            elif x<y:
                print(y-x)
                heapq.heappush(max_Heap, x-y)
        return -max_Heap[0] if max_Heap else 0
        