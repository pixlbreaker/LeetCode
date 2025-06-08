# Last updated: 6/7/2025, 11:33:27 PM
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