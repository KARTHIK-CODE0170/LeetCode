class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [0,0]
        cnt = 0
        for i in mat:
            if sum(i) > res[1]:
                res = [cnt,sum(i)]
            cnt +=1
        return res

        