from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    subset = []

    def backtrack(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        
        # include nums[i]
        subset.append(nums[i])
        backtrack(i+1)

        # not include nums[i]
        subset.pop()
        backtrack(i+1)

    backtrack(0)
    return res