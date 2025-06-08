# Last updated: 6/7/2025, 11:33:57 PM
class Solution:
    def hammingWeight(self, n: int) -> int:

        # string of bits
        s = self.intToBit(n)

        # counts how many 1's
        return s.count('1')
    
    # Converts ints to bits
    def intToBit(self, n) -> str:
        return "{0:b}".format(n)