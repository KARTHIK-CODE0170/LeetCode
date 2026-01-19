class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for i in range(len(costs)):
            if(costs[i] <= coins):
                coins = coins - costs[i]
                res += 1
            else:
                break
        return res
