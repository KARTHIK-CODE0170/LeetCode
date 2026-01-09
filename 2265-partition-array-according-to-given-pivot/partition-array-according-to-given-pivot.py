class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr = []
        idx = 0
        for i in nums:
            if i < pivot:
                arr.insert(idx, i)
                idx += 1
            elif i == pivot:
                arr.insert(idx, i)
            else:
                arr.append(i)
        return arr
