# Last updated: 3/27/2025, 11:24:31 AM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k:
            nums.insert(0, nums.pop())
            k -= 1
        