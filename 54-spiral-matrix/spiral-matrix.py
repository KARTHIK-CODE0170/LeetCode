class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix),len(matrix[0])
        res = list()
        top,bottom = 0,m
        left,right = 0,n
        #We are having 4loops for the traversal of the all the 4stages in the loop
        while(top < bottom and left < right):
            #left to right
            l = left
            while(l < right):
                res.append(matrix[top][l])
                l += 1
            top += 1

            #top to bottom
            u = top
            while(u < bottom):
                res.append(matrix[u][right - 1])
                u += 1
            right -= 1
            
            #right to left
            if top < bottom:
                r = right - 1
                while(r >= left):
                    res.append(matrix[bottom-1][r])
                    r -= 1
                bottom -= 1

            #bottom to top
            if left < right: 
                b = bottom - 1
                while(b >= top):
                    res.append(matrix[b][left])
                    b -= 1
                left += 1
        return res




            
            
                
