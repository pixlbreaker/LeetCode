# Last updated: 3/23/2025, 3:52:50 PM
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        writeIndex = m + n - 1
        m, n = m-1, n-1

        while n>=0 and m>=0:
            if nums1[m] > nums2[n]:
                nums1[writeIndex] = nums1[m]
                #nums1[m] = float("-inf")           We don't need to change this value because m will be pointing to m-1
                m -= 1
            else:
                nums1[writeIndex] = nums2[n]
                n -= 1
            writeIndex -= 1

        if n>-1:
            nums1[0:n+1] = nums2[0:n+1]
        
        