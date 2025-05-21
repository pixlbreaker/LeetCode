# Last updated: 5/21/2025, 4:41:03 PM
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
