class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        low = 0
        n = len(people)
        high = n - 1
        cnt = 0
        while low <= high:
            val = people[low] + people[high]
            if val <= limit or low == high:
                cnt += 1
                low += 1
                high -=1
            else:
                cnt += 1
                high -=1
        return cnt

