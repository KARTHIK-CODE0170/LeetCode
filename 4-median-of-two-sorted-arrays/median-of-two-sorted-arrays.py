class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if n & 1:
            return nums1[n//2]
        else:
            x = n//2
            return (nums1[x - 1] + nums1[x])/ 2