### Question
- [Link to question.](https://leetcode.com/problems/permutations/description/)

### Thoughts
- Input and output:
    - Input: the list of all numbers.
    - Output: the list of all possible permutations.
- If the list length is 1, return that list encapsulated in a list.
- The idea: choose the 1st number to be "the fixed number" at that position. Find the permutation of the rest, then at the end when we have all the permutations available, append the fixed number to each of the permutation and that all of that to the result.
- Example: [1,2,3]
    - Choose 1 as the fixed_num at position 1. Find the permutation of [2,3]
    - The permutation of [2,3] are [2,3] and [3,2]. Add 1 back to each of them. So if we fixed 1 as the 1st number, we have [1,2,3] and [1,3,2] as the permutations that can be added to the result.
    - Do the same thing when we fixed 2 as the first number and 3 as the first number.
- How to do that?
    - Pop the 1st number out of the list.
    - Find the permutations the rest of the numbers.
    - Add back 1st number to each of the permutation and add those permutations to the result.
    - Add the 1st number back to the list, but this time at the end of the list.
    - Come back from step 1 again, until we go through the length of the list.
- How can this work?
    - At first, we pop 1 out of the list. then find the permutation of [2,3].
    - We add 1 back to the list but to the end of it, so the list now becomes [2,3,1]
    - When we pop the first element of the list again, this time the fixed number will be 2.
    - Similarly, next time it will be 3.
    - After 3 rounds (the length of the list), we stop. 

### Pseudocode
- Initialize res = []
- The base case: if there's only 1 element in the list, return [nums[:]]
- Go through the length of the list
    - Pop out the 1st element in the list.
    - Recursively call the function on the list (now missing the 1st element) to find the permutations of the list without the 1st element.
    - After getting all the permutations, add back the 1st element to each permutation. Add those permutations to the result.
    - Add back the 1st element to the end of the list.
- Return result.

### BigO
- Find N! permutations with N calls => O(N*N!)