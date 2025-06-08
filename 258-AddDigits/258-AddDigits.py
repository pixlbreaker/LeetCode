# Last updated: 6/7/2025, 11:33:49 PM
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        sum = 0
        for i in str(num):
            sum += int(i)
        return self.addDigits(sum)
        