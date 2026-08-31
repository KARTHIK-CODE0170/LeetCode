class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        high = 2 * (10 ** 9)
        low = 1
        cnt = 0
        while low <= high:
            mid = (high - low)//2 + low
            cnt =(mid//a) + (mid//b) + (mid //c) -(mid//math.lcm(a,b))-(mid//math.lcm(a,c))-(mid//math.lcm(c,b)) + (mid//math.lcm(a,b,c))
            # if cnt == n:
            #     return mid
            if cnt >= n:
                high = mid - 1
            else:
                low = mid + 1
        return low

        