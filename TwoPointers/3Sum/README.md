### Question
- Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
- Notice that the solution set must not contain duplicate triplets.
- [Link to question.](https://leetcode.com/problems/3sum/)

### Thoughts
- Input and output:
    - Input: 
        - A list of numbers in sorted order.
        - A target (int)
    - Output: a list with 2 integers, represents the 2 indices(+1) of the numbers in the list that add up to the target.
- A bit similar to 2Sum but now there are 3 numbers. And there can be more than one answer, just no duplicate for each answer.
- In 2Sum, when the array is sorted, we can use 2 pointers to find the pair that adds up to the target.
- Can apply a similar method, with a little extra steps:
    - Since all numbers need to add up to 0, choose 1 number and pretend that will be in the result set.
    - Reset target. For example, if we choose -1, then the other 2 number need to add up to 1, so -1 + 1 = 0. Target becomes -1 for the other 2 number.
    - Now the question becomes 2Sum, with target set to (0-num).
- To do this, we need to sort the list first. Then go through the list. Pretend the current number is in the result set. Recalculate target, then find the 2 numbers (from the i+1 position to the end) to add up to the new target.
    - Tricky part is there will be duplicates in this list. Duplicates number will lead to potential duplicate solution.
    - Since the list is sorted, duplicates will stay next to each other.
        - Should check to see if the current number is a duplicate of the previous number. If it is, skip.
        - There can be multiple solutions for the current number. Instead of twosum where we found a solution then return immediately (the assumption of 2Sum was that there's only a unique solution), we need to search the whole array from postion i+1 to end to exhaust all solution.
- Example: [-1,0,1,2,-1,-4]. 
    - Sort list, it becomes [-4,-1,-1,0,1,2]
    - i=0: num=-4, new_taret = 0-(-4) = 4. Find 2 numbers that add up to 4 in the list, from i=1:end
        - Using 2Sum with 2 pointers, found []
    - i=1: num=-1. New target = 0-(-1) = 1. Find 2 numbers that add up to 1 in the list, from i=2:end
        - Using 2Sum with 2 pointers, found [-1,2] => Add [-1,-1,-2] to result.
        - Found another set [-1,0,1]
    - i=2: num=-1. Duplicate. Skip
    ...
    
### Pseudocode
- If len(nums) < 1: return []
- Sort the list.
- Loop through the list:
    - If this is not position 0 and the current number is equal to the previous number (dupliocates): skip
    - If not:
        - Calculate new target
        - Apply 2Sum with list[i+1:], new target.
            - If we find a result, append to the result list.
            - Continue to search because there can be more. 
                - Move left pointer up, right pointer down.
                - If the next position of the left point has the same value as the current position, we move up left pointer (we will have the same set of result if we count this number).
            - Move left pointer up if the 2sum < target
            - Move right pointer down if the 2sum > target
        - Add to result if 2Sum return something.
- Return result.

### BigO
- 2Sum runs in O(N) times. We run 2Sum at N elements => O(N^2).
- 2Sum takes O(1) space. At each position we only keep track of the current number => O(1) space.


