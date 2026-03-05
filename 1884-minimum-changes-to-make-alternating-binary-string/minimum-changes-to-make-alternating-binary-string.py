class Solution:
    def minOperations(self, s: str) -> int:
        One = 0
        x = len(s)
        for i in range(x):
            if((i % 2 == 0 and s[i] == '1') or (i % 2 != 0 and s[i] == '0')):
               One += 1
        # We find the difference of one pattern, in this case we found the with '10101010...' series

        return min(One,x - One)
        #The return is done for the optimal solution as we found the difference of one series the another one will be 
        #return (Total length of that minus the current difference)