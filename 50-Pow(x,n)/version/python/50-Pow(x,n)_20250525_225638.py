# Last updated: 5/25/2025, 10:56:38 PM
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        N = n
        if N < 0:
            x = 1 / x
            N = -N
        res = 1.0
        while N > 0:
            if N & 1:
                res *= x
            x *= x
            N >>= 1
        return res
        