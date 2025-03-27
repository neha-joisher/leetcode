class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x=[(r[0],r[2])for r in rectangles]
        y=[(r[1],r[3])for r in rectangles]

        x.sort()
        y.sort()

        def count_overlapping_intervals(intervals):
            prev=-1
            count=0
            for start,end in intervals:
                if prev<=start:
                    count+=1
                prev=max(prev,end)
            return count


        return max(count_overlapping_intervals(x),count_overlapping_intervals(y))>=3

        