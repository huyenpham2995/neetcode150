### Question
- A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
- Given a string s, return true if it is a palindrome, or false otherwise.
- [Link to question.](https://leetcode.com/problems/valid-palindrome/description/)

### Thoughts
- Input and output:
    - Input: a string
    - Output: a boolean, if the string is a palindrome.

### Pseudocode
- If the list is empty, return a list of an empty list.
- convert the string into all lowercases
- Initialize variables:
    - p1 for pointer going from the beginning
    - p2 for pointer going from the end
- loop through the string from the beginning and end and compare the letters:
    - if the character is not alphanumeric, move the pointer until we reach an alpha numeric letter.
    - Do the same with p2.
    - Compare p1 and p2. If the character are not equal, the string is not palindrome.
- If we reach the end, that means the string is palindrome.

### BigO
- Go through the string 1 time => O(N).
