# Last updated: 6/7/2025, 11:33:35 PM
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        # Double Reverse
        reversed1 = int(str(num)[::-1])
        reversed2 = int(str(reversed1)[::-1])

        if reversed2 == num:
            return True
        
        return False