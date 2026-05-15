class Solution:
    def produce(self,last,res,tot,stage) -> None:
        i = 0
        temp = [1]
        while i < len(last) and i < stage - 2 :
            x = last[i] + last[i + 1]
            temp.append(x)
            i += 1
        temp.append(1)
        res.append(temp)

    def generate(self, numRows: int) -> List[List[int]]:
        res = list()
        if numRows == 1:
            res.append([1])
            return res
        else:
            res.append([1])
            res.append([1,1])

        for s in range(3,numRows + 1):
            self.produce(res[-1],res,numRows,s)

        return res