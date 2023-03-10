### Question
- [Link to question.](https://leetcode.com/problems/palindrome-partitioning/description/)

### Thoughts
- Input and output:
    - Input: a string
    - Output: a list of palindrome substrings partitioned from the string.
- First of all, we need a function to determine if a given string is a palindrome.
    - Pointer at the start and end.
    - Compare the character at position start and position end, if they dont match the string is not palindrome.
    - Move start pointer forward and end pointer backward each time until they meet each other. Return True if all of them matches.
- Basically we want to partition the string at point i. If the substring from 0 to i is a palindrome, then we find another set of palindrome within the string from the i+1 position and go on until we reached the end of the string.
- If the substring from 0 to i is not a palindrome, the we move i forward and check the substring from 0 to i+1 and so on.
- Example: "aab"
    - i=0, j=0 (i be the starter point of the substring, j be the end point). The substring from i->j is a, which is a palindrome. Now we find more palindrome from the rest (ab).
    - Because the last substring is a palindrome, we will move both i and j up. i=1, j start at i=1
        - The substring from i->j is a, and it is a palindrome.
    - Because the last substring is a palindrome, we will move both i and j up. i=2, j start at i=2
        - The substring from i->j is b, and it is a palindrome.
    - Move up i and j, i=3, j=i=3. We reach the end of the string, we have the first partition [a,a,b].
    - Back to i=1, let's try j=2. The substring is ab, which is not a palindrome. 
        - Move j=3. Reach the end of string so just come back.
    - Back to i=0
        - j = 1: aa is a palindrome, add to the current partition [aa]
        - i=j=2: Check the rest of the string, which is b. b is a palindrome. Add to current partition [aa,b]
        - i=j=3, end of string, have another set [aa,b] in result.
    ...

### Pseudocode
- Initialize:
    - res = []: keep track of all partitions
    - p = []: keep track of each partitions and will be added to p when there's 1 valid partition
- Create a recursion function taking position i as parameter:
    - if i goes out of bound (>= len(s)), then append the copy of the current partition to res and return. (We reach the end of the string, nothing more to search).
    - Go through the string from position i to the end:
        - if the string from position i to j is palindrome, add it to p, then recursively search for another palindrome from position j+1 to the end.
            - pop the substring we just added to p for further searching (i.e clean up).
        - if it's not a palindrome, simply move j forward.
- Return res

### BigO
- Checking for each substring to see if it's palindrome takes N time at most (with N being the length of the string).
- We check all substrings, there are 2^N substrings in total (at each position, you have a choice to take or not take the current letter).
=> O(n *2^N).
