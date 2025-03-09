class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        # print([(i.start, i.end) for i in intervals])
        # for i in intervals:
        #     print(i.start,i.end)
        i,j=0,1
        while(j<len(intervals)):
            if intervals[i][1]>intervals[j][0]:
                return False
            else:
                i=j
            j+=1
        return True
        