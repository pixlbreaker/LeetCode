# Last updated: 3/24/2025, 4:20:39 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        check = True
        while check:
            
            if val in nums:
                nums.remove(val)
            else:
                check = False
        return len(nums)
        
        