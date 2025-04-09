# Last updated: 4/9/2025, 3:02:39 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = []

        for i in nums1:
            if i in nums2:
                if not i in inter:
                    inter.append(i)
        
        return inter