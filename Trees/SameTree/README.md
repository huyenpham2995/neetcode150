### Question
- [Link to question.](https://leetcode.com/problems/balanced-binary-tree/description/)

### Thoughts
- Input and output: 
    - Input: root of 2 binary trees.
    - Output: boolean, if the trees are the same (structure and value).
- My thoughts: 
    - At the current node of each tree, see if they are None. if they are all None then that's true, if only 1 of them are None then that's false.
    - If they are both having values, compare to see the value are the same.
    - Recursively checking their left and right nodes.


### Pseudocode
- At each node:
    - If they are all None, True. If one of them are None, then that's False.
    - If they are both having values, compare the value. if they are not equal return False.
- Recursively calling the function on their left side.
- Recursively calling the function on their left side.
- The result is the and operation between the results of those 2 calls.


### BigO
O(2N) = O(N) (N being the maximum number of nodes of each tree.)