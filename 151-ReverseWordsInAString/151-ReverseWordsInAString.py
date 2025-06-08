# Last updated: 6/7/2025, 11:34:00 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        
        # Converts to a list and reverses
        words = s.split(' ')
        words = list(filter(None, words))
        words.reverse()
        
        # Converst back to a string
        reverse = " ".join(words)
        return reverse