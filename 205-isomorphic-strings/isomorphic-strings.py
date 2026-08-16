class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = dict()
        for i,j in zip(s,t):
            x = freq.get(i,0)
            if x == 0 and j not in freq.values():
                freq[i] = j
            elif x != j:
                return False
        return True

        