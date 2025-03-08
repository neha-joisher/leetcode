class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
    
        intervals.sort()  # Sort intervals by start time
        res = [intervals[0]]  # Start with the first interval
        
        for i in range(1, len(intervals)):
            prev = res[-1]  # Last interval in the result list
            curr = intervals[i]  # Current interval
            
            if prev[1] >= curr[0]:  # Overlapping intervals
                res[-1] = [prev[0], max(prev[1], curr[1])]
            else:
                res.append(curr)
        
        return res
        # i=0
        # j=1
        # res=[]
        # intervals.sort()
        # while j <len(intervals):
        #     if intervals[i][1] < intervals[j][0]:
        #         res.append(intervals[i])
        #     else:
        #         intervals[j]=[min(intervals[i][0],intervals[j][0]),max(intervals[i][1],intervals[j][1])]
        #     i=j
        #     j+=1
        # res.append(intervals[j-1])
        # return res
#O(NLogN)