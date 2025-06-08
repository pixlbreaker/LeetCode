# Last updated: 6/7/2025, 11:33:50 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        for i in range(len(s)):
            c = s[i]
            if c in t:
                pos = t.find(c)
                t = t[:pos] + t[(pos+1):]
            else:
                return False
        return True