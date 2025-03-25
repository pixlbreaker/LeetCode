# Last updated: 3/25/2025, 4:58:58 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = len(nums) / 2
        num_dict = {}
        for i in nums:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = 1
        return max(num_dict, key=num_dict.get)