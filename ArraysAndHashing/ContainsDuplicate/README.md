### Question
- Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
[Link to question.](https://leetcode.com/problems/contains-duplicate/)

### Thoughts
- Input and output:
    - Input: array of int
    - Output: boolean to see if there's duplicate.
- Questions:
    - Can the array be empty? Yes.
- if array is empty or only has 1 element then no duplicates.
- Approach 1: go through the list, keep the count of each number in a dictionary. Any number has coun > 1 => duplicate. If at the end there's no number like that, then no duplicate.
- Approach 2: sort the list. Duplicate element will be next to each other.

### BigO
- Approach 1: O(N) runtime, O(N) space complexity.
- Approach 2: O(NlogN) runtime (time to sort), O(1) space complexity (only keep track of 2 numbers next to each other no matter how long the list is.)