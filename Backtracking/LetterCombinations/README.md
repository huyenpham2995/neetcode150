### Question
- [Link to question.](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)

### Thoughts
- Input and output:
    - Input: a string which is the combination of numbers from 2-9
    - Output: a list of all possible letter combinations that the number could represent.
- Mistake I made: The letter have to be in order of the given numbers. For example for string "23", one of the results should be "ad" BUT no "da", because 2 comes before 3. My solution included "da".
- Basically having a string which is a combination of 1 letter made from 2, 1 letter made from 3, etc. When the length of that combo string is equal to the length of the given string, we found 1 possible combination.
- We will go through the given string in order: grab 1 letter from 1st number, 1 letter from 2nd number and so on until we have grabbed a letter from all the numbers, then go back and do it again.
- We also need a mapping from the beginning for each number. eg: 2 maps to "abc", 3 maps to "def", etc.
- Example: 2,3
    - 2 can maps to a, b or c. We will try it one by one
        - If we map 2 to a
            - There are 3 options to match with 3: ad, ae, af
        - if we map 2 to b
            - There are 3 options to match with 3: bd, be, bf
        - if we map 2 to c
            - There are 3 options to match with 3: cd, ce, cf

### Pseudocode
- Initialize:
    - res = []: to get all the results.
    - combo = "": keep track of the combinations we find
- Create a backtrack recursive function, taking i as its index
    - if the length of combo is the same as the length of digits, append combo to res (we found a combination).
    - Start a loop to go through all characters available for the current digits
        - add the character to the combo
        - Recrusively call backtrack, passing in index i+1 (the next digit in the digits string)
        - remove the character out of the combo.
- call backtrack starting at 0
- return res    

### BigO
- The number of combinations we have: at most 1 number maps to 4 characters (9-wxyz). Let N be the length of the digits string. Find all combination at 1 number takes 4^N time at most, the length of each substring is N so O(N * 4^N).
