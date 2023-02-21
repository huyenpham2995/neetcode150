### Question
- [Link to question.](https://leetcode.com/problems/diameter-of-binary-tree/description/)

### Thoughts
- Input and output: 
    - Input: root of a binary tree.
    - Output: the length of its "diameter".
- Diameter is the length of the longest path between any two nodes in the tree (does not necessary have to go through root).
- Approach 1 (my approach):
    - The diameter is the maximum between the diameter of the left subtree, right subtree and the tree from the root.
    - The diameter is the sum of the maxDepth on the left + maxDepth on the right.
    - Recursively calculate the maxDepth, take the sum, then compare them to the left and right root to find the final max depth.
    - This approach will do a lot of repetitive work, since when you calculate the max depth at a ndoe, you already calculate the max depth of the left and the right. 
- Approach 2: no repetitive work.
    - Similar idea, but at each level they calculate the diameter and save that result to the next level.
    - Also calculate the height at each node right away.

### Pseudocode
#### Approach 1
- Calculate the diameter at the current node by taking maxDepth of the left + maxDepth of the right.
- Compare it to the left subtree and right subtree (calling diameter function recursively).
- Return the max

#### Approach 2
- Keep a global vaiable res = 0
- At each node:
    - Recursively do a dfs at left node, calculate the height of that node.
    - Recursively do a dfs at right node, calculate the height of that node.
    - Diameter = max(current_diameter, height left + height right).

### BigO
- O(N) for approach 2.

