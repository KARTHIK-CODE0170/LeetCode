class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        freq = dict()
        for i in arr:
            freq[i] = bin(i).count("1")
        def sort_key(x):
            return (freq[x], x)
        
        arr.sort(key=sort_key)
        
        return arr

                