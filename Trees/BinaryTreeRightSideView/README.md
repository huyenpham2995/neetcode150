### Question
- [Link to question.](https://leetcode.com/problems/binary-tree-right-side-view/description/)

### Thoughts
- Input and output: 
    - Input: root of a binary tree.
    - Output: the list of values from the right side view.
- If the tree is empty then return an empty list.
- My thought: using BFS
    - This is pretty similar to the Tree traversal by level order.
    - We can travel in the order of root-right-left.
    - At each level, record all the nodes of that level. The right side view is the one at position 0 of the root-right-left traversal.
    - At each node, add its right children to the next_q first, then its left children. if it doesn't have a children on either side, don't add anything. The right side view will just be the first element of the next_q.

### Pseudocode
- If root is None return [].
- Initialize variables:
    - res = []
    - q = []
- While the q is not empty 
    - Append the first element of the q to the result list (right most node).
    - Have a local variable called next_q to hold the next queue to be processed.
    - Go through all nodes in the queue:
        - Add the node right child if it's not None.
        - Add the node left child if it's not None.
    - Set q = next_q
- Return res.

### BigO
- O(N).

