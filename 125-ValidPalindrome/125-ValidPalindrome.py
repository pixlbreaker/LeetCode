# Last updated: 6/7/2025, 11:34:03 PM
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        n = len(alpha)
        for i in range(n//2):
            if not (alpha[i] == alpha[n-1-i]):
                return False
        
        return True