# Last updated: 6/7/2025, 11:33:23 PM
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = sum(nums)

        digitSum = 0
        for i in nums:
            for c in str(i):
                j = int(c)
                digitSum += j
        
        return abs(elementSum - digitSum)