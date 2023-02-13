### Question
- You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
- Evaluate the expression. Return an integer that represents the value of the expression.
- Note that:
    - The valid operators are '+', '-', '*', and '/'.
    - Each operand may be an integer or another expression.
    - The division between two integers always truncates toward zero.
    - There will not be any division by zero.
    - The input represents a valid arithmetic expression in a reverse polish notation.
    - The answer and all the intermediate calculations can be represented in a 32-bit integer.
- [Link to question.](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

### Thoughts
- Input and output:
    - Input: list of tokens (signs and numbers).
    - Output: an integer after calculation.
- Question:
    - Can the list be empty? Yes, can just return 0.
    - What if the division gives a decimal number? Only take the division part. So 5/3 is 1, not 1,333333.
- It's pretty straightforward. Everytime I encounter a number, I put it in the stack. If it's not a number, then it is an operand. And operand involve 2 closest numbers that we encounter, so we would just need to pop the most current 2 out of the stack and did an operation on them, then push the result number back to the stack. Do that until the end.
- The corner case here would be when the number is negative. So all of the elements in the tokens array is string. To check if they are numbers, we can call isdigit() on each of them. But if they are negative number, for example isdigit("-11") will return False, even though it is a valid negative integer.
    - First need to check if the string length > 1 (the string can just contain the operand "-").
    - The check if it starts with -.
    - Then convert the rest to integer, and take 0 - that integer to change it to negative integer.
    
### Pseudocode
- If the length of tokens < 1, return 0.
- Assign an empty list as the number_stack to store numbers.
- Go through all tokens:
    - if it's negative integer (length > 1, starts with "-" and the rest are digits):
        - Convert the part except the first character ("-") to integer, then take 0-that integer and add that to the number_stack.
    - If it's positive integer string: convert it to integer.
    - If it's not a number, it's prob a token:
        - Pop 2 elements out of number_stack (the first one is added after, so that's num2, the 2nd pop is num1)
        - Depends on the operand, do `num1 <operand> num1`.
            - if the operand is "/", only take the division.
    - Push the result back to number_stack and continue to the end.
- Return the only number in the number_stack (the result).

### BigO
- Go through each token once => O(N) runtime.
- number_stack will store at most N elements => O(N) space.



