### Question
- [Link to question.](https://leetcode.com/problems/balanced-binary-tree/description/)

### Thoughts
- Input and output: 
    - Input: root of a binary tree.
    - Output: boolean, if the tree is balanced.
- Diameter is the length of the longest path between any two nodes in the tree (does not necessary have to go through root).
- learn from the previous problem to find the diameter, at each level of recursion, remember the maximum diff to see if that goes beyond 1.

### Pseudocode
- Keep a global vaiable diff = 0
- At each node:
    - Recursively do a dfs at left node, calculate the height of that node.
    - Recursively do a dfs at right node, calculate the height of that node.
    - Keep track of the diff between the height from the left and right. If the diff is > 1 then the tree is imbalanced.

### BigO
O(N)