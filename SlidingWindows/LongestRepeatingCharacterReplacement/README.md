### Question
[Link to question.](https://leetcode.com/problems/longest-repeating-character-replacement/)

### Thoughts
- Input and output:
    - Input: 
        - A string.
        - An int indicates how many letters that can be replaced.
    - Output: the longest repeating character with replacement.
- If the string is empty or just 1 character, the longest number will just be the length of the string because there is nothing that we can replaced.
- Example "ABBB", k=2:
    - We can replace A with B to create BBBB, and that will have the length of 4 repeating character.
    - We can also have another option of replacing B with A. Since there are 2 replacements allowed, we can create AAAB, which have the length of 3.
    - So which one will we go for? We are aiming to keep the character that has the most appearance in the string, and replace the rest with the amount of k that we are allow.
    - So if we only have A at first, we save the count of A:1, and keep it, since it's the character with the most appearance so far.
    - Now if we move on and have AB, we save A:1, B:1. The most count is still 1, so we can either keep A or B. Either way, we will replace 1, so we have 1 more chance to replace (k=2).
    - Now move on to ABB, we save A:1. B:2. The most count is 2, which means we should replace A for B. We still have 1 more chance to replace. Longest is 3.
    - Move on to ABBB, we save A:1, B:3. The most count is 3, which means we should replace A for B. We still have 1 more chance to replace. Longest is 4.
    - Reaching the end, return 4.
- Example: AABABBA, k=1
    - A: A:1, keep A. 1 chance to replace. Longest = 1
    - AA: A:2. keep A. 1 chance to replace. Longest = 2
    - AAB: A:2, B:1. Keep A, replace B. No chance to replace. Longest = 3
    - AABA: A:3, B:1. Keep A, replace B. No chance to replace. Longest = 4.
    - AABAB: A:3, B:2, replace B. But we have no chance to replace left.
        - Move up the window for the string to become ABAB (remove the 1st A).
        - Update the count so A:2, B:2.
    - ABABB: A:2, B:3, replace A. But we have no chance to replace left.
        - Move up the window for the string to become BABB (remove A).
        - Update count: A:1. B:3.
    - BABBA: A:2, B:3, replace A. But we have no chance to replace left. 
        - Move up the window for the string to become ABBA (remove B).
        - Update count: A:2, B:2.
    - End of the string. Max length = 4.

### Pseudocode
- If length string < 2: return length string.
- Initialize variables:
    - l,r = 0,0
    - count {}
    - max_length = 0
- r from 0->length of s:
    - Add s[r] to count.
    - Calculate the max_char_len (the character that appears the most in the current substring from l->r). It's either the current character we just added to the count dict, or the existing character with max length.
    - Calculate the number of characters we have to replace: r-l+1 (the length of the window) - max_char_len (the # of appearances of the most repeating character.). Check to see if it's > k.
        - If it is, we cannot replace anymore character. That's when we shift the window by moving l 1 step to the right, and update count[s[l]] -= 1.
    - Calculate the current max length.
- return max_length

### BigO
- Travel through the string once with r pointer => O(N).
- Might travel 1 more time with l pointer => O(2N) = O(N).

