class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i=0
        j=1
        res=[]
        intervals.sort()
        while j <len(intervals):
            if intervals[i][1] < intervals[j][0]:
                res.append(intervals[i])
            else:
                intervals[j]=[min(intervals[i][0],intervals[j][0]),max(intervals[i][1],intervals[j][1])]
            i=j
            j+=1
        res.append(intervals[j-1])
        return res
#O(NLogN)