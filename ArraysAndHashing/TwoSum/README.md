### Question
- Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
- You may assume that each input would have exactly one solution, and you may not use the same element twice.
- You can return the answer in any order.
- [Link to question.](https://leetcode.com/problems/two-sum/description/)

### Thoughts
- Input and output:
    - Input: array of int, an integer `target`
    - Output: an array of 2 indicies that add up to `target`.
- Questions:
    - What if the array is empty? Returning value will be empty.
    - Can the number be negative? yup.
    - What if there are more than 1 solution? In this question we assume there's only 1 solution.
- Go through each number and check the rest to see if that number + any other numbers in the list add up to the target.
    - Start at the first number.
    - Go from 2nd to last number to see if 1st number + ith number = target.
    - Do that with all the number on this the list until we reached the end.
- Instead of loop through all other numbers and find their sum, we can take `target` - current_num and see if the result number is in the list.
    - Save all numbers in a dictionary.
    - Calculate `target` - current_num = result.
    - Find result in the dictionary.

### BigO
- Approach 1: at each number, we go through all of the other number => runtime O(N^2).
- Approach 2: save each number and its position in a dictionary takes O(N) time.
    - Loop through each number and find the result number take O(N) time.
    => O(N)
