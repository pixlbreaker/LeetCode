# Last updated: 4/10/2025, 6:42:10 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if not i in nums:
                return i
        
        return n