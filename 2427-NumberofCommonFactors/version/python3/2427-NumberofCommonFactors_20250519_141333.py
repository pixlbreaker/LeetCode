# Last updated: 5/19/2025, 2:13:33 PM
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        a_factors = self.getFactors(a)
        b_factors = self.getFactors(b)

        
        return len(set(a_factors) & set(b_factors))
    
    def getFactors(self, n: int):

        lst = []
        for i in range(1, n+1):
            if n % i == 0:
                lst.append(i)
        
        return lst