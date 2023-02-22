### Question
- [Link to question.](https://leetcode.com/problems/validate-binary-search-tree/description/)

### Thoughts
- Input and output: 
    - Input: root of a binary tree.
    - Output: boolean, if the tree is BST
- First attempt: DFS, at each node see if the left node < node < right node. If node is None then return True.
    - Apparently this is not enough because you have to make sure ALL nodes on the left is less than root and ALL nodes on the right is larger than the root.
- To do this, we need to keep the bound at each node we are visiting.
- Example: tree [5,1,6,null,null,3,7]
    - At 5, the bound is -inf < 5 < inf because it is the root so no constraint.
    - At 1, the bound is -inf < 1 < 5 (1 is on the left of 5 so it has a right bound which is 5).
    - On the other side, at 6 the bound is 5 < 6 < inf (on the right of 5 so it has a left bound which is 5).
    - At 3, the bound is 5<3<6 (the bound carry from its parent which is 6). 3 is not > 5 so this is not a binary search tree.

### Pseudocode
- Create a subfunction to help with keeping track of the bound.
- If root is None return True.
- Initialize left = -inf, right = inf
- Starting at root, check to see if left < node.val < right
- If it is, call recursive function on left and right node
    - For left node: call function with the same left, but set right bound = cur_node.val
    - For right node: call function with same right, but set left bound = cur_node.val

### BigO
O(N)