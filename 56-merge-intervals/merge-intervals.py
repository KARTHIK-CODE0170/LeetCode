class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = list()
        i = 0
        while i < len(intervals):
            x = intervals[i][0]
            y = intervals[i][1]
            j = i + 1
            while(j < len(intervals)):
                if y < intervals[j][0]:
                    break
                else:
                    y = max(y,intervals[j][1])              
                j +=1
            res.append([x,y])
            i = j            
        return res

        