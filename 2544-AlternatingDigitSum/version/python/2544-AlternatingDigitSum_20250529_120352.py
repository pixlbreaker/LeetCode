# Last updated: 5/29/2025, 12:03:52 PM
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