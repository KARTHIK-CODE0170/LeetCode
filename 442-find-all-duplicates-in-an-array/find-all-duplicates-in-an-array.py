class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        arr = [0] * len(nums)
        for i in range (len(nums)):
            if not arr[nums[i] - 1]:
                arr[nums[i] - 1] = 1
            else:
                res.append(nums[i])
        return res

