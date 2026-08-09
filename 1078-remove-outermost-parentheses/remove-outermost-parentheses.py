from collections import deque
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arr = []
        flag = 0
        for i in s:
            if i == '(':
                if flag > 0:
                    arr.append(i)
                flag += 1
            else:
                flag -= 1
                if flag > 0:
                    arr.append(i)
        return ''.join(arr)
