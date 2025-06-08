# Last updated: 6/7/2025, 11:33:29 PM
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        lst = list(str(n))
        sum = 0
        sign = 1

        for i in lst:
            digit = int(i) * sign
            sum += digit
            sign *= -1

        return sum