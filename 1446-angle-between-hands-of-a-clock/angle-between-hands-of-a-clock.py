class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hr_pos = (hour * 30) + (minutes * 0.5)
        mi_pos = (minutes * 6)
        res = abs((hr_pos%360) - (mi_pos % 360))
        res = min(res,abs(360-res))
        return res
