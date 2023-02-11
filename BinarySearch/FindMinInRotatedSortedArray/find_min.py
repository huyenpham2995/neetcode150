from typing import List

def find_min(nums: List[int]) -> int:
    if len(nums) == 1: return nums[0]

    l, r = 0, len(nums)-1
    min_val = float("inf")

    while l<=r:
        mid = (l+r)//2
        # print(mid)
        min_val = min(nums[mid], min_val)
        if nums[mid] < nums[r]:
            r = mid -1
        else:
            l = mid + 1
    
    return min_val
        