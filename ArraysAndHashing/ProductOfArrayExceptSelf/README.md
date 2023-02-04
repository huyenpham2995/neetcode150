### Question
- Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
- You must write an algorithm that runs in O(n) time and without using the division operation.
- [Link to question.](https://leetcode.com/problems/product-of-array-except-self/description/)

### Thoughts
- Input and output:
    - Input: a list of numbers
    - Output: a list of products, where location i contains the product of all numbers in the list except the number at list[i]
- My 1st thought: we can compute the product of all numbers in the given list, then at each location, divide the product to the number of that location.
    - This will satisfy the condition for runtime O(N), but we used division.
- Better approach: got it after some hints. Example: [1,2,3,4]
    - At 1, we need the product of [2,3,4]
    - At 2, we need the product of [1,3,4] an so on. 
    - If we just look at left side at one time and right side at one time, we have:
        - On the left, going from beginning to end:
            - At 1, we dont need any number on the left (can just set the product to 1)
            - At 2, we need product of 1
            - At 3, we need product of [1,2]
            - At 4, we need product of [1,2,3]
        - On the right, and going from end to beginning:
            - At 4, we dont need any number on the right (can just set the product to 1)
            - At 3, we need product of 4
            - At 2, we need product of [4,3]
            - At 1, we need product of [4,3,1]
    - For each number, if we take the product of what we have on the left with what we have on the right, we get the product we need.
    - Note that as we move, the product we need at the current position is just the product of the previous position * itself.

### Pseudocode
- If the list is empty, return a list of an empty list.
- Initialize variables:
    - A left_product = 1
    - A right_product = 1
    - result = []
- Loop through the number from beginning to end (compute left product):
    - result[i] = left_product
    - left_product *= nums[i] # calculating for the next position, since current product don't include itself, i.e nums[i]
- Loop through the number from end to beginning (compute right product):
    - result[i] *= right_product (take left product * right product)
    - right_product *= nums[i]
- Return result.

### BigO
- Going through the number from beginning to end takes O(N).
- Going through the number from end to beginning takes O(N).
- Overall O(N).
