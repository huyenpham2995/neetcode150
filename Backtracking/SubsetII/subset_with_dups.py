from typing import List

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    res = set()
    subset = []
    nums.sort()

    def backtrack(i):
        if i >= len(nums):
            res.add(tuple(subset.copy()))
            return
        
        # take nums[i]
        subset.append(nums[i])
        backtrack(i+1)

        # not taking nums[i]
        subset.pop()
        backtrack(i+1)
    
    backtrack(0)

    return list(res)