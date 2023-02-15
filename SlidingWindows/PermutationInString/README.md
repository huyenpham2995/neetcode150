### Question
[Link to question.](https://leetcode.com/problems/permutation-in-string/description/)

### Thoughts
- Input and output:
    - Input: 2 strings.
    - Output: boolean, if one contains the permutation of the other.
- Need s1 to be shorter than s2, because if it's longer there's no way s2 can "contain" the permutation of s1.
- Approach 1: my approach.
    - Turn s1 into a list of characters. Go through s2 and if the character is in that list in a streak, pop it out of the list. If the list becomes empty, return True. If not false.
    - Some things to consider:
        - if s1 is "ab" and the s1 contains "acb", then we already pop a out of the list at that point.
        - Need to add a back into the list before moving on to b to continue to check.
        - Will need a left pointer to stand at the point where the streak potentially "starts". 
            - If the streak ends before the list is empty, add back whatever character from l to r to the list.
    - Example: s2="dcda", s1="acd"
        - Turn s1 into list, i.e [d,c,a].
        - l=r=0. s2[r] = d in list. Pop d out so list becomes [c,a]. r += 1
        - l=0, r=1. s2[r] = c in list. Pop c out so list becomes [a]. r += 1
        - l=0, r=2. s2[r] = d not in the list. Now increment l and add the character at l back to the list. List becomes [d,a].
        - l=1, r=2. s2[r] = d in list. Pop d out so list becomes [a]. r += 1
        - l=1, r=3. s2[r] = a in list. Pop c out so list becomes []. r += 1
        - List is empty so return True.
- Approach 2: O(26N) approach, with N being the length of s2.


### Pseudocode

### BigO


