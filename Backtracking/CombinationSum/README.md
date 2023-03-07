### Question
- [Link to question.](https://leetcode.com/problems/combination-sum/description/)

### Thoughts
- Input and output:
    - Input: 
        - the list of all numbers (candidates).
        - the target.
    - Output: the list of all possible combinations that sum up to target.
- If there is no candidate, then return [] (nothing can make up the target).
- Since we can duplicate a number as much as we could, we can keep grabbing that number until the sum is > target.
- At each position, we have 2 choices: taking or not taking the current number.
- Example: candidates = [2,3,6,7], target = 7
    - At i=0, take 2. sum=2 < target, combo = [2]
        - Take another 2, combo = [2,2]. sum=4 < target
        - Take another 2, combo = [2,2,2]. sum=6 < target
        - Take another 2, combo = [2,2,2,2]. sum=8 > target
        - Not taking another 2, pop 2, combo = [2,2,2] sum=6. move on to i=1
    - At i=1, take 3, combo = [2,2,2,3] sum=9 > target.
        - Not taking 3, pop 3, combo = [2,2,2] sum=6. move on to i=2
    - At i=2, take 6, combo=[2,2,2,6] sum=12 > target
        - Not taking 6, pop 6, combo = [2,2,2] sum=6. move on to i=3
    - At i=3, take 7, combo=[2,2,2,7] sum=13 > target
        - Not taking 7, pop 7, combo = [2,2,2] sum=6. move on to i=4.
    - i=4 >= len(candidates), come back to i=3.
    - At i=3 already pop 7 out, come back to i=2
    - At i=2 already pop 6 out, come back to i=1
    - At i=1, pop another 2 out (don't take that 2), combo = [2,2], sum=4
        - sum < target, take candidates[2]
    ... 
    Keep going on and backtracking where we haven't tried adding and not adding the current number.

### Pseudocode
- Initialize variable:
    - sum = 0
    - combo = []
    - res = []
- Create function backtrack for recursion, taking index i as parameter.
    - if i>= len(candidates) return
    - option 1: take the current candidate
        - Add candidate[i] to sum
        - Append candidate[i] to combo
        - if sum == target: add the current combo to result
        - if sum < target: call backtrack with current i to add another candidate[i] to the combo
    - option 2: not taking the current candidate:
        - pop candidate[i] out of combo
        - take out candidate[i] from current sum
        - move on to call backtrack on i+1
- return res

### BigO
