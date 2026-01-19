class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if(sum(costs) <= coins):
            return len(costs)
        costs.sort()
        res = 0
        for i in range(len(costs)):
            if(costs[i] <= coins):
                coins = coins - costs[i]
                res += 1
            else:
                break
        return res
