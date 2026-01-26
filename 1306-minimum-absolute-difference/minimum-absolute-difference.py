class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        n = len(arr)
        arr.sort()
        min_diff = float('inf')
        for i in range(1,n):
            min_diff = min(min_diff,arr[i] - arr[i - 1])
        res = []
        for i in range(1,n):
            if(arr[i] - arr[i - 1] == min_diff):
                res.append([arr[i-1],arr[i]])
        return res if min_diff != float('inf') else []
        