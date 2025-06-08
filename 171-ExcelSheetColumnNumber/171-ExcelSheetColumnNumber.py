# Last updated: 6/7/2025, 11:33:59 PM
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum = 0
        n=1
        for i in range(len(columnTitle)-1, -1, -1):
            sum += n * (ord(columnTitle[i])-64)
            n = n * 26
        return sum