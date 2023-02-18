### Question
- [Link to question.](https://leetcode.com/problems/invert-binary-tree/description/)

### Thoughts
- Input and output: 
    - Input: root of a binary tree.
    - Output: root of the tree after inverting all the elements.
- Back to the basic. The base case is when the root node is None, then just return None.
- This is tree traversal/recursion. At each root, we swap the left and the right node. Then call the exact function on the left node (now it is the root of the new function), the right node. After all swap are completed, return the root.

### Pseudocode
- Check if root is None, return None.
- root.left, root.right = root.right, root.left
- Call invert_tree(root.left)
- Call invert_tree(root.right)
- When done return root.

### BigO
- Visit each node once, O(N).


