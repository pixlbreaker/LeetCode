# Last updated: 6/7/2025, 11:33:33 PM
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
        if num1 == 0 or num2 == 0:
            return 0

        if (num1 >= num2):
            num1 = num1 - num2
        else:
            num2 = num2 - num1

        return self.countOperations(num1, num2) + 1        
