# Last updated: 6/7/2025, 11:33:38 PM
class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        count = 0
        coinsInRow = 1
        rows = 0

        while count <= n:
            count += coinsInRow

            coinsInRow += 1
            rows += 1
        
        return rows-1
