# Last updated: 4/24/2025, 4:28:24 PM
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
            
        for i in range(num):
            if i * i == num:
                return True
            if i * i > num:
                return False
        
        return False