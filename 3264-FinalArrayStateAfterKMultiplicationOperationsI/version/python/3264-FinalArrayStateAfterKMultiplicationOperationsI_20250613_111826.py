# Last updated: 6/13/2025, 11:18:26 AM
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        for i in range(k):

            # Update and find the min
            new_min = min(nums) * multiplier
            index = nums.index(min(nums))
            
            # Update the list
            nums[index] = new_min
        
        return nums