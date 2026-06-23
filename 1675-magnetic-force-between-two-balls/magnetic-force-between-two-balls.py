class Solution:
    def fun(self,arr,balls,mid):
        cnt = 1
        lastpos = arr[0]
        for i in range(1,len(arr)):
            if arr[i] - lastpos >= mid:
                cnt += 1
                lastpos = arr[i]
            if cnt == balls:
                return True
        return False
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        ans = -1
        low, high = 1, position[-1] - position[0]
        while low <= high:
            mid = low + (high - low) //2
            if self.fun(position,m,mid):
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        return ans