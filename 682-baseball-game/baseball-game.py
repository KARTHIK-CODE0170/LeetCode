class Solution:
    def calPoints(self, arr: List[str]) -> int:
        res = []
        for i in range(len(arr)):
            if arr[i] == "D":
                res.append((res[-1]) * 2)
            elif arr[i] == 'C':
                res.pop()
            elif arr[i] == '+':
                res.append(res[-1] + res[-2])
            else:
                res.append(int(arr[i]))
        return sum(res)
