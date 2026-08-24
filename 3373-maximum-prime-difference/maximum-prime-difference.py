arr = [True] * 101
prime = set()
arr[0] = arr[1] = False
i = 2
while i <= 101:
    j = i * i
    while j <= 101:
        arr[j] = False
        j += i
    i += 1   
for i in range(len(arr)) :
    if arr[i]:
        prime.add(i)
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        first = last = -1
        for i in range(len(nums)):
            if nums[i] in prime:
                if first == -1:
                    first = i
                else:
                    last = i
        if first != -1 and last != -1:
            return last - first
        else:
            return 0

        
        