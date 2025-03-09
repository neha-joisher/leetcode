class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:


        intervals.sort()
        minheap=[]

        for i in intervals:
            if minheap and minheap[0]<=i[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap,i[1])
        return len(minheap)

        # if not intervals:
        #     return 0
        # intervals.sort()
        # res=[intervals[0]]
        # j=1
        # flag=False
        # while(j<len(intervals)):
        #     flag=False
        #     for i,x in enumerate(res):
        #         if len(x)==2 and x[-1]<=intervals[j][0] or len(x)>2 and x[-1][1]<=intervals[j][0]:
        #             flag=True
        #             res[i].append(intervals[j])
        #             break
        #     if flag==False:
        #         res.append(intervals[j])
        #     j+=1
        # return len(res)
        