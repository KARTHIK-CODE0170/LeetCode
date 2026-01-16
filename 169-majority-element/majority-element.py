class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = 0
        count = 0
        for i in nums:
            if(count == 0):
                num = i
            if(num == i):
                count += 1
            else:
                count -= 1
        return num
            