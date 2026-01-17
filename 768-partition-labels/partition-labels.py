class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occ = dict()
        res = []
        for i in range(len(s) - 1,-1,-1):
            if not (s[i] in last_occ):
                last_occ[s[i]] = i
        i = 0
        while(i < len(s)):
            last = last_occ[s[i]]
            left = i
            while(left  <= last):
                if(last_occ[s[left]] > last):
                    last = last_occ[s[left]]
                left += 1
            res.append(left - i)
            i = left
        return res