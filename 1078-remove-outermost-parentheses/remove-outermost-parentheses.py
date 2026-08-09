from collections import deque
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arr = []
        flag = 0
        for i in s:
            if flag == 0 and i == "(":
                flag += 1
            elif i == "(":
                arr.append(i)
                flag += 1
            elif i == ")" and flag - 1 == 0:
                # arr.append(i)
                flag -= 1
            else:
                arr.append(i)
                flag -= 1
        return ''.join(arr)
