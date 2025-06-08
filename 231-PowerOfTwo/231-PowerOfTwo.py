# Last updated: 6/7/2025, 11:33:51 PM
import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False
        if n == 1:
            return True
        
        x = math.log2(n)
        return (x).is_integer()