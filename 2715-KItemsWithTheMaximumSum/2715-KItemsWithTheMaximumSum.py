# Last updated: 6/7/2025, 11:33:22 PM
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        if numOnes >= k:
            return k
        
        remainder = k - numOnes - numZeros
        if remainder <= 0:
            return numOnes
        
        return numOnes - remainder