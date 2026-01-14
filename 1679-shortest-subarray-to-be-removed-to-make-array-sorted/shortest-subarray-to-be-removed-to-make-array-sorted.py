class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left,right = 1,n -1
        while(left < n and arr[left] >= arr[left - 1]):
            left += 1
        while(right > 0 and arr[right] >= arr[right-1]):
            right -= 1
        
        left -= 1
        res = min(right,n - left - 1)
        l,r = 0,right

        while(l <= left and r < n):
            if(arr[l] <= arr[r]):
                res = min(res,r-l-1)
                l+= 1
            else:
                r +=1

        return 0 if (res <= 0) else res
 