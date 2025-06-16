# Last updated: 6/16/2025, 11:18:24 AM
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        lst = list(str(n))
        prod = 1
        sums = 0
        for i in lst:
            prod *= int(i)
            sums += int(i)
        
        return prod - sums