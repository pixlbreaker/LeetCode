# Last updated: 4/11/2025, 12:18:16 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        
        # Converts to a list and reverses
        words = s.split(' ')
        words = list(filter(None, words))
        words.reverse()
        
        # Converst back to a string
        reverse = " ".join(words)
        return reverse