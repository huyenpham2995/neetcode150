### Question
- [Link to question.](https://leetcode.com/problems/subsets-ii/description/)

### Thoughts
- Input and output:
    - Input: the list of all numbers.
    - Output: the list of all possible subsets without duplicate subsets.
- This is very similar to subsets, but the difference is that there will be duplicates in the original array, which will lead to the duplicates in the subsets. And we don't allow duplicated subsets.
- We can basically collect the subsets like we did before, but this time the result list will be a set. The property of a set is that it does not allow duplicates, so when we add a duplicate in the set it will just be 1.
- Another corner case that the set won't catch is [1,4] and [4,1]. To catch this, before finding all the subsets, we can sort the nums array in order. Once it is sorted, we will guarantee only the case of [1,4] will appear, not [4,1].

### Pseudocode
- Initialize:
    - res = set()
    - subset = []
    - sort nums array.
- define a recursive function backtrack that takes index i as its parameter
    - if i >= len(nums) then add subset to result.
    - option 1: take nums[i]
        - Add it to the subset
        - Recursively call the function at i += 1
    - option 2: not take nums[i]
        - Pop it out of the subset.
        - Call the recursive function at i += 1
- Call backtrack and passing in 0.
- Convert res into array instead of set. Return res.

### BigO
- Sort the array O(NlogN).
- Go through all the element in the array nums and create 2^N subsets => O(Nx2^N).
