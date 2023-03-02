from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    def helper(start: int, end: int, nums: List[int], k: int):
        if start >= end: return nums[end]

        p = start
        pivot = nums[end]

        for i in range(start,end):
            if nums[i] < pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        
        nums[p], nums[end] = nums[end], nums[p]
        if p == len(nums) - k:
            return nums[p]
        if p < len(nums) - k:
            return helper(p+1, end, nums, k)
        return helper(start, p-1, nums, k)
    
    return helper(0, len(nums)-1, nums, k)