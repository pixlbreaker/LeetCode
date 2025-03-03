class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        less = []
        more = []
        target = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                less.append(nums[i])
            elif nums[i] > pivot:
                more.append(nums[i])
            else:
                target.append(nums[i])

        return less + target + more