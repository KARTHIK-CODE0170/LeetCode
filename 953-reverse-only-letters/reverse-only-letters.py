class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)
        # fun = []
        fun = list(x for x in s if x.isalpha())
        fun = fun[::-1]
        s = list(s)
        j = 0
        for i in range(n):
            if s[i].isalpha():
                s[i] = fun[j]
                j += 1
        return "".join(s)