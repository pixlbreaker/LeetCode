# Last updated: 6/3/2025, 10:24:38 PM
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        dividing = []
        for i in range(left, right + 1):
            if self.isSelfDividing(i):
                dividing.append(i)

        return dividing
    
    def isSelfDividing(self, num):
        lst = list(str(num))

        if '0' in lst:
            return False

        for i in lst:
            if num % int(i) != 0:
                return False
        
        return True