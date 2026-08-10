class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        arr = [[0 for _ in range(n)] for _ in range(n)]
        top = left = 0
        right = down = n-1
        i = j = 0
        val = 1
        while left <= right and top <= down:
            #row left to right
            j = left
            while j <= right:
                arr[i][j] =val
                j += 1
                val += 1
            top += 1
            i = top
            j -= 1
            #col top to bottom
            while i <= down:
                arr[i][j] = val
                i += 1
                val += 1
            right -= 1
            i -= 1
            #right to left bottom

            if left <= right:
                j = right
                while j >= left:
                    arr[i][j] = val
                    val += 1
                    j -= 1
                down -= 1
                j += 1
            if top <= down:
                i = down
                while i >= top:
                    arr[i][j] = val
                    val += 1
                    i -= 1
                left  += 1
                i += 1
        return arr


