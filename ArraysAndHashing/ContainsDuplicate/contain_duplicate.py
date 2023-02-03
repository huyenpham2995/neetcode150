from typing import List 
from collections import defaultdict

def containsDuplicate1(nums: List[int]) -> bool:
    if len(nums) < 2: return False

    count_dict = defaultdict(int)
    for num in nums:
        count_dict[num] += 1
        if count_dict[num] > 1:
            return True

    return False

def containsDuplicate2(nums: List[int]) -> bool:
    if len(nums) < 2: return False
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False