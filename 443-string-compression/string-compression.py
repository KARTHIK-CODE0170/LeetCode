class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        cnt = 0
        left = 0
        right = 1
        if len(chars) == 1:
            return 1
        while left <= right and right < len(chars):
            if chars[right] != chars[right - 1]:
                if right - left == 1:
                    s += chars[right - 1]
                else:
                    s += chars[right - 1]
                    s += str(right - left)
                left = right
            right += 1
        if right - left != 1:
            s += chars[right - 1]
            s += str(right - left)
        else:
            s += chars[right - 1]
        slen = len(s)
        for i in range(slen):
            chars[i] = s[i]
        return slen
                



        