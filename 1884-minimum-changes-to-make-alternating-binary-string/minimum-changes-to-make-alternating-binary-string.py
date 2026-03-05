class Solution:
    def minOperations(self, s: str) -> int:
        One = ""
        Zero = ""
        x = len(s)
        for i in range(x):
            if(i % 2 == 0):
                One += '1'
                Zero += '0'
            else:
                One += '0'
                Zero += '1'
        oc = zc = 0
        for i in range(x):
            if(One[i] != s[i]):
                oc += 1
            elif(Zero[i] != s[i]):
                zc += 1
        return min(oc,zc)
        