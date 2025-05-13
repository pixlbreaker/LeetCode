# Last updated: 5/13/2025, 12:30:21 PM
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        # Double Reverse
        reversed1 = int(str(num)[::-1])
        reversed2 = int(str(reversed1)[::-1])

        if reversed2 == num:
            return True
        
        return False