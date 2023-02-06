from typing import List

def longest_consecutive(nums: List[int]) -> int:
    if len(nums) <2: return len(nums)
    nums_set = set(nums)
    max_count = 1

    for num in nums_set:
        if num-1 not in nums_set:
            next_num = num + 1
            count = 1
            while next_num in nums_set:
                count += 1
                next_num +=1
            if count > max_count:
                max_count = count
    
    return max_count