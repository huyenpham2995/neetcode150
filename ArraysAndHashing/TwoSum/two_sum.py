from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    if len(nums) == 0: return []
    num_dict = {}

    for i in range(len(nums)):
        num2 = target - nums[i]
        if num2 in num_dict.keys():
            return [num_dict[num2], i]
        num_dict[nums[i]] = i
    
    return []