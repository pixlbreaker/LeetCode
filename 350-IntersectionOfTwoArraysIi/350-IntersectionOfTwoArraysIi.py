# Last updated: 6/7/2025, 11:33:42 PM
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = []
        x = nums1 if len(nums1) > len(nums2) else nums2
        y = nums2 if len(nums1) > len(nums2) else nums1
        for i in y:
            if i in x:
                inter.append(i)
                x.remove(i)
        return inter