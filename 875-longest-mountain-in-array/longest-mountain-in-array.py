class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        inc = dec = 0
        left = 0
        dis = 0
        ans = 0
        while left < n - 1:
            if left < n - 1 and arr[left] == arr[left + 1]:
                left+= 1
                continue
            if left < n - 1 and arr[left] < arr[left + 1]   :
                while left < n - 1 and arr[left] < arr[left + 1]:
                    inc = 1
                    dis += 1
                    left += 1
                while left < n - 1 and arr[left] > arr[left + 1] :
                    dec = 1
                    dis += 1
                    left += 1
                if inc == 1 and dec == 1:
                    ans = max(ans,dis + 1)
                dis = 0
                inc = 0
                dec = 0
            else:
                left += 1    
        return ans
