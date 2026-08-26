class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        res = 0
        for i in s:
            if i == "(":
                cnt += 1
            if i == ")":
                cnt -= 1
            res = max(res,cnt)
        return res
        