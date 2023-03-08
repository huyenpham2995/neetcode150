from typing import List

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    combo = []
    candidates.sort()

    def backtrack(i, target):
        if target == 0:
            res.append(combo.copy())
            return
        if i>= len(candidates) or target <= 0:
            return

        pre = -1
        for j in range(i,len(candidates)):
            if candidates[j] == pre:
                continue
            combo.append(candidates[j])
            backtrack(j+1, target - candidates[j])
            combo.pop()
            pre = candidates[j]
    
    backtrack(0,target)
    return res