# Last updated: 6/1/2025, 7:32:42 PM
class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        digits = list(str(num))

        for i in digits:
            if num % int(i) == 0:
                count += 1
        
        return count