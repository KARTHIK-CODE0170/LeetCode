class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = 0
        cnt = 0
        for i in nums:
            if cnt == 0:
                maj = i
                cnt += 1
            elif maj != i:
                cnt -= 1
            else:
                cnt += 1
        return maj