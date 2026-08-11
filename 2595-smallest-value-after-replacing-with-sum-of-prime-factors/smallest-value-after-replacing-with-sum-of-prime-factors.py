class Solution:
    def god(self,n):
        arr = []
        for i in range(n + 1):
            arr.append(i)
        i = 2
        while i * i <= n:
            # if arr[i] == i:
            j = i * i
            while j <= n:
                if arr[j] == j:
                    arr[j] = i
                j += i
            i += 1
        return arr
    
    def smallestValue(self, n: int) -> int:
        arr = self.god(n)
        i = n
        while arr[i] != i:
            j = i
            sumi = 0
            while j > 1:
                sumi += arr[j]
                j = j // arr[j]
            if i == sumi:
                break
            
            i = sumi

        return i

    

        