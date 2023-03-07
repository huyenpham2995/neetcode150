from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    sum = 0
    combo = []
    res = []

    def backtrack(i):
        nonlocal sum
        if i >= len(candidates): return
        
        sum += candidates[i]
        combo.append(candidates[i])
        if sum == target:
            res.append(combo.copy())
        elif sum < target:
            backtrack(i)
        combo.pop()
        sum -= candidates[i]
        backtrack(i+1)
    
    backtrack(0)
    return res