class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        for i, x in enumerate(intervals):
            if x[1] < newInterval[0]:  # No overlap, before newInterval
                res.append(x)
            elif x[0] > newInterval[1]:  # No overlap, after newInterval
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            else:  # Overlapping intervals, merge
                newInterval = [min(x[0], newInterval[0]), max(x[1], newInterval[1])]

        res.append(newInterval)
        return res