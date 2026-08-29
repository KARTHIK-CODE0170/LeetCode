class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        arr = list()
        for i in range(len(nums) - 2):
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            else:
                j,k = i + 1,len(nums)-1
                target = -nums[i]
                while(j < k):
                    x = nums[j] + nums[k]
                    if(x == target):
                        arr.append([nums[i],nums[j],nums[k]])
                        j += 1
                        k -= 1
                        while(j < k and nums[j] == nums[j-1]):
                            j += 1
                        while(j < k and nums[k] == nums[k+1]):
                            k -= 1
                    elif x > target:
                        k -= 1
                    else:
                        j += 1

        return arr       