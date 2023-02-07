### Question
- Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
- Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
- The tests are generated such that there is exactly one solution. You may not use the same element twice.
- Your solution must use only constant extra space.
- [Link to question.](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

### Thoughts
- Input and output:
    - Input: 
        - A list of numbers in sorted order.
        - A target (int)
    - Output: a list with 2 integers, represents the 2 indices(+1) of the numbers in the list that add up to the target.
- Questions:
    - Can the list be empty? Yes, then nothing add to the target.
    - Can the numbers be negative? Yes.
- We can basically use binary search to search for the other half.
    - For each number, search for (target-number) in the array. Since the array is sorted, we can use binary search to search for the 2nd number. 
    - Binary search takes O(logn) time, so overall for n numbers it will take O(nlogn).
- An optimized way:
    - Since the array is sorted, we know if we add 2 numbers and the sum of it is lower than the target, we need to increase one of them and vice versa.
    - If we have 2 pointers, 1 at the beginning (i.e at the position of the smallest number), 1 at the end (at the position of the largest number).
        - If the sum is too small compares to target, increase the position of pointer 1 (pointer 2 is already at the biggest number)/
        - If the sum is too large compares to target, decrease the position of pointer 2.
        - Keep doing that until we meet the target, or if not the 2 pointer will meet each other.
    - Example: [2,7,11,15], target = 9
        - p1 at 2, p2 at 15. 2+15 = 15 > 9, we decrease p2.
        - p1 at 2, p2 at 11. 2+11 = 13 > 9, we decrease p2.
        - p1 at 2, p2 at 7. 2+7=9 == 9. Return [1,2]

### Pseudocode
- If the list is empty, return [].
- Initialize variables:
    - p1=0, p2=len(nums) - 1.
- When p1 < p2
    - if nums[p1] + nums[p2] == target: return [p1+1, p2+1]
    - if nums[p1] + nums[p2] < target: p1++
    - if nums[p1] + nums[p2] > target: p2--
- If we reach the end and still dont find the result, then there's no pairs satisfy the question.

### BigO
- 2 pointers go through the array just 1 time => O(N).

