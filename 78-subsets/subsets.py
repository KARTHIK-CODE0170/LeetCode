class Solution:
    def god(self,nums,res,arr,idx):
        if idx == len(nums):
            res.append(arr.copy())
            return
        
        arr.append(nums[idx])
        self.god(nums,res,arr,idx+1)
        arr.pop()
        self.god(nums,res,arr,idx +1)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.god(nums,res,[],0)
        return res
        