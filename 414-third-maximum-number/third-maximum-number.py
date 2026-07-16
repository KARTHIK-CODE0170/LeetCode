class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        last = mid = first = float('-inf')
        for i in nums:
            if first == i or mid == i or last == i:
                continue 
            if first < i:
                first, mid, last = i, first,mid
            elif i > mid:
                mid, last = i , mid
            elif i > last:
                last = i
        return last if last != float('-inf') else first
        