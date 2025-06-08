# Last updated: 6/7/2025, 11:33:40 PM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        lowest = sorted(d.items(), key=lambda x: x[1])[0]
        if lowest[1] == 1:
            return s.index(str(lowest[0]))
        else:
            return -1