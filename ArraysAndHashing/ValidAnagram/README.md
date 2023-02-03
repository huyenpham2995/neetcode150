### Question
- Given two strings s and t, return true if t is an anagram of s, and false otherwise.
- An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.[Link to question.](https://leetcode.com/problems/valid-anagram/)

### Thoughts
- Input and output:
    - Input: 2 strings s and t.
    - Output: boolean, if they are anagram.
- if the length of the 2 strings are different, they are not anagram.
- Can either or both of them be empty? Sure. If they are both empty then they are anagram.
- If t is the anagram is s, the number of all the letters in t are the same as the number of that letters in s.
    - We need to count the occurence of each letter in t, and in s.
    - Compare those counts. If all of them are the same then t is an anagram of s.
- Same theory, when t is the anagram of s, if we sort that t and s, then both string should look exactly the same.
    - Sort both strings.
    - Compares letter by letter.

### BigO
- Approach 1: O(N) time and O(N) space (for storing the counts).
- Approach 2: O(NlogN) for sorting the strings, O(1) space (only comparing 2 letters at a time).
