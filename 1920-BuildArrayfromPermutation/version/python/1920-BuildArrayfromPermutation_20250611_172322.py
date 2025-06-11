# Last updated: 6/11/2025, 5:23:22 PM
class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0

        for i in range(0, len(s)-1):
            c = ord(s[i])
            c2 = ord(s[i+1])
            
            score += abs(c - c2)
        
        return score