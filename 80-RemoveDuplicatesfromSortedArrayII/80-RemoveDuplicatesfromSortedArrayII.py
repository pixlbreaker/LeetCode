# Last updated: 3/26/2025, 12:00:26 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Iterate double
        i = 2
        while i < len(nums):
            
            # Current and previous and previouss
            curr = nums[i]
            prev = nums[i-1]
            prevv = nums[i-2]

            # If there is a third one
            if curr == prev and curr == prevv:
                del nums[i]
            else:
                i += 1
        
        return len(nums)