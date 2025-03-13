class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        while count < 999:
            sum = self.getSum(n)
            n = sum
            if sum == 1:
                return True
            count += 1
        return False
    
    def getSum(self, n) -> int:
        sum = 0
        # Splits the number
        for d in str(n):
            sum += int(d)**2
        return sum