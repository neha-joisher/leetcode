class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()  # Sort intervals by start time
        res = [intervals[0]]  # Start with the first interval
        
        for i in range(1, len(intervals)):
            prev = res[-1]  # Last interval in the result list
            
            if prev[1] >= intervals[i][0]:  # Overlapping intervals
                res[-1] = [prev[0], max(prev[1], intervals[i][1])]
            else:
                res.append(intervals[i])
        
        return res
