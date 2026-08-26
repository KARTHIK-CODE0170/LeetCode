class Solution:
    def frequencySort(self, s: str) -> str:
        freq = dict()
        for i in s:
            freq[i] = freq.get(i,0) + 1 
        
        new_freq = {k:v for k,v in sorted(freq.items(),key=lambda x : (-x[1],ord(x[0])))}
        res = []
        for i,j in new_freq.items() :
            res.append(i*j)
        return ''.join(res)
        