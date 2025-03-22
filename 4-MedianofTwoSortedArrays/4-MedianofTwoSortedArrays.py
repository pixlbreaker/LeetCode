// Last updated: 3/22/2025, 3:32:12 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merged the lists and sorts them
        mergedlist = nums1 + nums2
        mergedlist.sort()
        
        # Finds the median
        if len(mergedlist) % 2 == 1:
            return mergedlist[len(mergedlist)//2]
        else:
            mid1 = mergedlist[len(mergedlist)//2 - 1]
            mid2 = mergedlist[len(mergedlist)//2]
            
            return (mid1+mid2)/2
        