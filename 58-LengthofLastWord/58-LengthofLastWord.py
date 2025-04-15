# Last updated: 4/15/2025, 4:40:28 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split(' ')
        lst = list(filter(lambda x: x != "", lst))
        return len(lst[-1])