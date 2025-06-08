# Last updated: 6/7/2025, 11:33:30 PM
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return n*2