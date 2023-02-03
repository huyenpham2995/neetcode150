### Question
- Given an array of strings strs, group the anagrams together. You can return the answer in any order.
- An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
- [Link to question.](https://leetcode.com/problems/group-anagrams/description/)

### Thoughts
- Input and output:
    - Input: a list of strings.
    - Output: a list of all the groups of anagrams.
- Since anagram is formed by reordering an existed word, they technically has the same set of letters. To find the groups of anagrams, we can sort each string separately. All the strings that are anagram of each other will be exactly the same after sorting.
- Since there are different groups, there should be a data structure to each group separately.
    - The key of each group can be the string after being sorted (since after sorting they are the same).
    - The value is the original words.
- After that we can just pack all the groups into a big list and return it.

### Pseudocode
- If the list is empty, return a list of an empty list.
- Initialize variables:
    - A dictionary with key as a string, value as a list.
- Go through each word in the list
    - Sort that word so the letters are in alphabetical order, then save that to a variable called sorted_word.
    - Check to see that sorted_word key existed.
    - Append the original word to the list of words that have the same sorted_word.
- At the end, make a big list of all the lists we have, based on sorted_word.

### BigO
- Go through all word in the list takes N times, with N being the length of the list.
    - Sort each word of different length. Let the word with longest characters be length of m => sorting takes O(Nmlogm)
    - So in total it takes O(Nmlogm)
- Go through the dictionary to get the compiled list takes at most O(N) time and this is a separate operation.
=> O(Nmlogm)
