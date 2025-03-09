class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
            if not intervals:
                return 0
            j=1
            count=0
            intervals.sort()
            res=intervals[0]
            for j in range(1,len(intervals)):
                if res[1]<=intervals[j][0]:
                    res=intervals[j]
                else:
                    count+=1
                    res=[res[0], min(intervals[j][1],res[1])]
            return (count)
        