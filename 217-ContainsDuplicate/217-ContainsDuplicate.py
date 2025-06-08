# Last updated: 6/7/2025, 11:33:53 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        if len(nums) == len(numSet):
            return False
        return True
            