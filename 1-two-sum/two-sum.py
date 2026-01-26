class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i in range(len(nums)):
            key = target - nums[i]
            if key in d :
                return [d[key],i]
            else:
                d[nums[i]] = i
        