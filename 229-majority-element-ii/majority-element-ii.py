class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = dict()
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1
        res = []
        limit = len(nums)//3
        for i in freq:
            if(freq[i] > limit):
                res.append(i)
        return res
        