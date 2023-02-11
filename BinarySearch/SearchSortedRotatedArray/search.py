from typing import List

def search(nums: List[int], target: int) -> int:
    l,r = 0, len(nums)-1

    while l<=r:
        mid = (l+r)//2
        if nums[mid] == target: return mid
        
        if nums[l] <= nums[mid]: # left side sorted
            if target < nums[mid] and nums[l] <= target: # left <= target < mid
                r = mid - 1
            else:
                l = mid + 1
        else:
            if target > nums[mid] and nums[r] >= target: # mid < target <= r
                l = mid + 1
            else:
                r = mid - 1
    return -1