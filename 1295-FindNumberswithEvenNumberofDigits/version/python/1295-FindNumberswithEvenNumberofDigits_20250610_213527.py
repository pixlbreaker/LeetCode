# Last updated: 6/10/2025, 9:35:27 PM
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        count = 0
        for i in nums:
            lst = list(str(i))
            if len(lst) % 2 == 0:
                count += 1
        
        return count
