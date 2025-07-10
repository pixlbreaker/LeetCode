# Last updated: 7/10/2025, 6:21:05 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for j in jewels:
            for i in stones:
                if j == i:
                    count += 1
        return count