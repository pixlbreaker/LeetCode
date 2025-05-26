# Last updated: 5/26/2025, 11:56:43 AM
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = sum(nums)

        digitSum = 0
        for i in nums:
            for c in str(i):
                j = int(c)
                digitSum += j
        
        return abs(elementSum - digitSum)