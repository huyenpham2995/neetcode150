### Question
- [Link to question.](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

### Thoughts
- Input and output: 
    - Input: root of a binary tree.
    - Output: root of the tree after inverting all the elements.
- Approach 1 (my approach): recursion
    - At each level, the depth of the current level is the maximum depth of the left child vs the right child + 1.
    - Why +1? Take into consideration the current level as well.
- Approach 2 (iterative with stack):

### Pseudocode
#### Approach 1
- Check to see if root is None. If it is return 0.
- Recursively calling the function and determine the depth by taking 1 + max(maxDepth(left), maxDepth(right)).

### BigO



