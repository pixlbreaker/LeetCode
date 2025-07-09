# Last updated: 7/9/2025, 3:40:36 PM
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        evenOdd = []

        for i in nums:
            if i % 2 == 0:
                evenOdd.append(0)
            else:
                evenOdd.append(1)
        
        evenOdd.sort()
        nums = evenOdd
        return nums