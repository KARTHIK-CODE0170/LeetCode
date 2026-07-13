class Solution:
    def spiralOrder(self, arr: List[List[int]]) -> List[int]:
        left = top = 0
        right = len(arr[0]) - 1
        down = len(arr) - 1
        res = []
        while left <= right and top <= down:
            i = left 
            while i <= right:   
                res.append(arr[top][i])
                i += 1
            top += 1
            i = top
            while i <= down:
                res.append(arr[i][right])
                i += 1
            right -= 1
            i = right
            if top <= down:
                while i >= left:
                    res.append(arr[down][i])
                    i -= 1
                down -= 1
            i = down
            if left <= right:
                while i >= top:
                    res.append(arr[i][left])
                    i -= 1
                left += 1
        return res
