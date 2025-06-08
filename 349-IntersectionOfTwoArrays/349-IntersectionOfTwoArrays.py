# Last updated: 6/7/2025, 11:33:43 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = []

        for i in nums1:
            if i in nums2:
                if not i in inter:
                    inter.append(i)
        
        return inter