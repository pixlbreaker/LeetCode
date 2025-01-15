class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = ""

        if len(s) == 1:
            return s
        for j in range(len(s)):
            for i in range(len(s), j, -1):
                sub = s[j:i]
                #print(sub)
                if self.isPalindrome(sub) and len(sub) > len(longest):
                    longest = sub
        
        return longest
    
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]