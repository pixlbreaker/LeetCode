# Last updated: 6/7/2025, 11:33:45 PM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(0, math.floor(n/2), 1):
            temp = s[i]
            s[i] = s[n-1-i]
            s[n-1-i] = temp
        