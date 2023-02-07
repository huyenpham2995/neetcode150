from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 2: return []
    nums = sorted(nums)
    result = []

    for i in range(len(nums)-1):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        new_target = 0-nums[i]
        p1 = i+1
        p2 = len(nums) -1

        while p1 < p2:
            if nums[p1] + nums[p2] == new_target:
                result.append([nums[i], nums[p1], nums[p2]])
                p1 += 1
                p2 -= 1
                while p1 < p2 and nums[p1] == nums[p1-1]:
                    p1 += 1
            elif nums[p1] + nums[p2] < new_target:
                p1 += 1
            else:
                p2 -= 1
    
    return result