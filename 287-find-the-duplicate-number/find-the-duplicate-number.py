class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = dict()
        for i in nums:
            if freq.get(i,0) + 1 > 1: 
                return i
            freq[i] = freq.get(i,0) + 1
        return 0
        