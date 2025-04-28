# Last updated: 4/28/2025, 6:48:11 PM
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output = ""
        if numRows == 1:
            return s
        elif numRows >= len(s):
            return s

        rows = [''] * min(numRows, len(s))
        i = 0
        down = False

        for c in s:
            rows[i] += c
            if i == 0 or i == numRows -1:
                down = not down
            if down:
                i += 1
            else:
                i -= 1

            
        output = ''.join(rows)
        return output