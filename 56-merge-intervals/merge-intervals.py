class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        res = []
        i = 0
        if n == 1:
            return intervals
        while(i < n):
            start = intervals[i][0]
            end = intervals[i][1]
            while i + 1 < n and intervals[i + 1][0] <= end: #OverLapping
                end = max(end,intervals[i+1][1])
                i += 1
            res.append([start,end])
            i+=1
        return res