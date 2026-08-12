class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n - 1
        while i < j:
            sumi =numbers[i] + numbers[j]
            if  sumi < target:
                i += 1
            elif sumi > target:
                j-=1
            else:
                return [i+1,j+1]