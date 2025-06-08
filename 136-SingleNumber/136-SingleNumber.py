# Last updated: 6/7/2025, 11:34:02 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while len(nums) > 0:
            val = nums.pop()
            if not val in nums:
                return val
            nums.insert(0, val)
        