class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year = bin(int(date[:4]))
        year = year[2:]
        month = bin(int(date[5:7]))
        month = month[2:]
        date = bin(int(date[8:10]))
        date = date[2:]
        return year + "-" + month + "-" + date