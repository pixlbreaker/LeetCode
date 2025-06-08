# Last updated: 6/7/2025, 11:33:37 PM
import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:

        # Sort and get the smallest and largest
        nums.sort()
        small = nums[0]
        large = nums[-1]

        # GCD
        return math.gcd(small, large)