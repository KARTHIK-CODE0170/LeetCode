class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left, right = 0, 0
        sumi = 0
        cnt = 0
        while right < len(arr):
            sumi += arr[right]
            if right - left + 1 == k:
                if sumi // k >= threshold:
                    cnt += 1
                sumi -= arr[left]
                left += 1
            
            right += 1
        return cnt            
            
