# Last updated: 5/28/2025, 10:20:01 AM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False

        if n == 1:
            return True

        if n % 4 == 0:
            return self.isPowerOfFour(n/4)
        else:
            return False