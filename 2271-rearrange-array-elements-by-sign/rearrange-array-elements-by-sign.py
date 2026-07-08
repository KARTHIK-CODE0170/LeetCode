class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        e, o = 0, 1
        res = [0] * len(nums)
        for i in nums:
            if i >= 0:
                res[e] = i
                e += 2
            else:
                res[o] = i
                o += 2
        return res

        