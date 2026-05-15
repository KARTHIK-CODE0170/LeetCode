class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mpp = {0:1}
        prefixsum = 0
        cnt  = 0
        for i in range(n):
            prefixsum += nums[i]
            remove = prefixsum - k
            if remove in mpp:
                cnt += mpp[remove]
            mpp[prefixsum] = mpp.get(prefixsum,0) + 1
        return cnt


