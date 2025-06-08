# Last updated: 6/7/2025, 11:33:46 PM
class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        bin_val = 0
        for i in range(n+1):
            val = bin(i)
            output.append(val.split('b')[-1].count('1'))
        return output
            
            
            
        