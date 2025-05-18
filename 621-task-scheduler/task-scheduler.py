class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_Map=Counter(tasks)
        max_Heap=[-value for value in freq_Map.values()]
        heapq.heapify(max_Heap)
        queue=collections.deque()
        t=0

        while max_Heap or queue:
            t+=1
            #no tasks available in the heap
            if not max_Heap:
                time = queue[0][1]
            else: 
                count=1+heapq.heappop(max_Heap)
                #if instances of task are remaining
                if count:
                    queue.append((count,t+n))
            #if t is equal to cooldown time for the first task
            if queue and t==queue[0][1]:
                heapq.heappush(max_Heap,queue.popleft()[0])
        return t
        
        