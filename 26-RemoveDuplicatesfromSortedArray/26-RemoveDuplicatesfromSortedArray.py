# Last updated: 3/24/2025, 4:21:13 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # Current number we are on
        i=0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1