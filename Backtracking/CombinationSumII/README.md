### Question
- [Link to question.](https://leetcode.com/problems/combination-sum-ii/description/)

### Thoughts
- Input and output:
    - Input: 
        - the list of all numbers (candidates).
        - the target.
    - Output: the list of all possible combinations that sum up to target.
- If there is no candidate, then return [] (nothing can make up the target).
- This is different than Combination Sum I since we can only use each number in the array 1 time (no duplicate). There can be duplicate in the array tho.
- The idea is slightly different: If we see a duplicate in the array, we skip processing it. In order to make sure that we don't skip on something that we have already processed, we can sort the array. The duplicated numbers stay next to each other, so if we already processed 1 of them, the others can be skipped. Another mechanism to avoid duplicates is that as we move on, we only add the numbers "forward" (the index is > than the index of the current number we are processing).
- Example: candidates = [2,5,2,1,2], target = 5.
    - After sorting, candidates become [1,2,2,2,5]. 
    - At 1, we will find the combination of [1,2,2].
    - At 2, we find no combination.
    - At 2, the process will repeat mostly the same. So since we already processed 2, we skip this.
    - At the last 2, skip.
    - At 5, we find [5].
- The core still looks like Combination I, where at which position we will decide either to take the number or not. The difference is that if we already processed the previous number the current number is the same, we skip the current number.

### Pseudocode
- Initialize:
    - res = []
    - combo = []
- Sort candidates
- Create a recrusive function backtrack, which takes in i as the current index, and target as the target we need to find the sum for.
    - if target == 0: (we found the combo that added up to target):
        - add the copy of the combo to res (adding copy since if we say res.append(combo), it will add the reference of combo to res, and combo and change moving forward).
        - return
    - if i >= len(candidates) or target <= 0 (index out of range, numbers added up exceeds target):
        - return
    - Set pre = -1 (no duplication at first)
    - Go through the list of the candidates from i to the end (we only want to process from current number onwards to avoid duplication from already processed number)
        - if candidates[i] == pre: we already processed this number, skip.
        - else:
            - Decision to take candidates[i]: 
                - append candidates[i] to combo
                - calling recursive function with i+1 and target - candidates[i] 
            - Decision not to take candidates[i]:
                - pop candidates[i] out of combo
                - set pre = candidates[i]
- call backtrack with initial value of i=0 and target=target
- return res

### BigO
- Still need to find 2^N combinations, so O(2^N).
