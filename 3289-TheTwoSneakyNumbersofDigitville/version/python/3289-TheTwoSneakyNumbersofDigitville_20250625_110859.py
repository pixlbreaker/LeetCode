# Last updated: 6/25/2025, 11:08:59 AM
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        lst = []
        sneak = []

        for i in nums:
            if i in lst:
                sneak.append(i)
            else:
                lst.append(i)
        
        return sneak