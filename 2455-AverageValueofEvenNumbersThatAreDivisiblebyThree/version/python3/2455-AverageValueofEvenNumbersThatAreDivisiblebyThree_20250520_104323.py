# Last updated: 5/20/2025, 10:43:23 AM
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        threeSum = 0
        count = 0

        for i in nums:
            if i % 3 == 0 and i % 2 == 0:
                threeSum += i
                count += 1
        
        if threeSum == 0:
            return 0
        
        return threeSum//count