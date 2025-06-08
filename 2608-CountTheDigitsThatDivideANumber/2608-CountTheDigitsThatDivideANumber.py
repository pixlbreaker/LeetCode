# Last updated: 6/7/2025, 11:33:24 PM
class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        digits = list(str(num))

        for i in digits:
            if num % int(i) == 0:
                count += 1
        
        return count