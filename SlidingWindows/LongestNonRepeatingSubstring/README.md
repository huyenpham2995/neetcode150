### Question
- [Link to question.](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

### Thoughts
- Input & output:
    - Input: a string.
    - Output: the length of the longest substring without repeating characters.
- If the string is empty, return 0.
- If the string has 1 character, return 1.
- 2 pointers, 1 at start and 1 at start + 1. 
    - Everytime we encounter an unique character, add it to a dictionary and keep the right one going.
    - Once we hit a character that is already in the dictionary, move the left pointer to the place of the duplicate character, then move left 1 more position. Calculate the length up until then (r-l).
    - Keep the right pointer continue until the end.
    - Return the maximum length.
- Example: s="abcabcbb"
    - l=0, r=1. {a:1}. s[r]=b not in the dictionary:
        - Add s[r] to dictionary. {a:1,b:1}.
        - Update r += 1 = 2.
    - l=0, r=2. s[r]=c not in the dictionary:
        - Add s[r] to dictionary. {a:1,b:1,c:1}.
        - Update r += 1 = 3.
    - l=0, r=3. s[r]=a is in the dictionary.
        - max_count = max(3-0, 0) = 3.
        - s[l] == s[r] = a, l < r so l+=1 = 1.
        - Update r=4
    - l=1, r=4. s[r]=b is in the dictionary.
        - max_count = max(4-1, 3) = 3.
        - s[l] == s[r] = b, l < r so l+=1 = 2.
        - Update r=5.
    - l=2, r=5. s[r]=c is in the dictionary.
        - max_count = max(5-2, 3) = 3.
        - s[l] == s[r] = c, l < r so l+=1 = 3.
        - Update r=6.
    - l=3, r=6. s[r]=b is in the dictionary.
        - max_count = max(6-3, 3) = 3.
        - s[l] = a != b. l+= 1 = 4.
        - s[l] == s[r] = b, l < r so l+=1 = 5.
        - Update r=7.
    - l=5, r=7. s[r]=b is in the dictionary.
        - max_count = max(7-5, 3) = 3.
        - s[l] = c != b, l+=1=6.
        - s[l] = b == s[r]. l < r so l+= 1=7.
        - Update r=8.
    - Stop. Return max_count.
### Pseudocode
- if len(s) < 2: return len(s)
- Initialize variables:
    - l,r=0,1
    - d = {s[l]:1}
    - max_count=0
- when l <= r < len(s)
    - if letter at r is not in dictionary (i.e not encounter before): add it to the dictionary.
    - Else
        - max_count = max(max_count, r-l)
        - keep l pointer going up until s[l] == s[r]
            - Reset the value for key at r to 0
        - if l < r: l+=1
    - update r += 1
- Return max_count

### BigO
- Go through all characters in the string with right pointer 1 time O(N).
- Might go through them 1 more time with left pointer => O(2N) =  O(N).
