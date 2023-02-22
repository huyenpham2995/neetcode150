### Question
- [Link to question.](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/)

### Thoughts
- Input and output: 
    - Input: root of a binary tree.
    - Output: count of the good nodes in the tree (there's no node from the path from root to this node that is > than this node).
- My approach: BFS
    - Having a queue to keep track of all nodes in the tree while traverse the tree in order.
    - At each node, keep track of the maximum value from the root to the current node. Check if the current value of the node is >= max value, then that is a good node.
    - Add the children of the current node (if any) in the queue for future processing.
- Another approach: DFS
    - If the node is None then return 0.
    - If the current value of node >= max_value then res = 1
    - Recursive calculate the result by taking res + calling function for node.left and node.right

### Pseudocode
#### Approach 1
- if root is None return 0
- Create a q with 1 element: (root, root.val) (node, max_val)
- set count = 0
- while q is not empty:
    - Pop first element out of queue.
    - check to see if the val is >= max_val, if it is +1 to count.
    - if node has left child, add (left node, left_node.val if left_node.val > max_val else max_val) to queue
    - if node has right child, add (right node, right_node.val if right_node.val > max_val else max_val) to queue
- Return count.

#### Approach 2
- Create a dfs recursive function:
    - if root is none return 0
    - res = 1 if current val > max_val else 0
    - Update max_val if root.val > max_val
    - res += call bfs on root.left and max_val
    - res += call bfs on root.right and max_val
    - return res
- From main function call dfs(root,root.val)

### BigO
- Both approaches go through all nodes once => O(N).

