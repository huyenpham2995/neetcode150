from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    res = []
    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        # Let the first number be the fixed number
        fixed_num = nums.pop(0)

        # find the permutation of the other 2
        perms = permute(nums)

        # append back the fixed number to each of the permutation
        for perm in perms:
            perm.append(fixed_num)
            res.append(perm)
        # since we pop the 1st element out of the array, it's time to add it back, but now to the end of the array (so we can process other number as fixed num)
        nums.append(fixed_num)
    
    return res