class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        ans = [0,0]
        for i in range(len(numbers) - 1):
            left = i + 1
            right = n - 1
            find = target - numbers[i]
            while left <= right:
                mid = (left + right)//2
                if numbers[mid] == find:
                    ans[0],ans[1]=i + 1,mid + 1
                    return ans
                elif numbers[mid] < find:
                    left = mid + 1
                else:
                    right = mid - 1
        return ans
